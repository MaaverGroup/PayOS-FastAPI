"""
───────────────────────────────────────────────────────────────
 🚀 Project: PayOS-FastAPI – FastAPI Serverless on Vercel
 🔗 GitHub: https://github.com/MaaverGroup/PayOS-FastAPI
 🧑‍💻 Author: Maaver Group
 🌐 Website: https://maaver.com
 📄 License: MIT
 📅 Created: 2025-04-09
───────────────────────────────────────────────────────────────

Description:
This FastAPI backend is designed to run serverlessly on Vercel,
enabling dynamic QR code payment creation using PayOS.

Deploy-ready, simple to configure via .env, and easily pluggable
into any frontend such as Next.js via API routes.
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from payos import PayOS, ItemData, PaymentData
from dotenv import load_dotenv
import os
import time

# ----------------------------------------------------------------------
# Load environment variables from .env file
# ----------------------------------------------------------------------
load_dotenv()

# ----------------------------------------------------------------------
# Required PayOS credentials (users should provide these in .env)
# ----------------------------------------------------------------------
client_id = os.getenv("PAYOS_CLIENT_ID")
api_key = os.getenv("PAYOS_API_KEY")
checksum_key = os.getenv("PAYOS_CHECKSUM_KEY")

# Validate credentials presence early
if not all([client_id, api_key, checksum_key]):
    raise ValueError("Missing PayOS credentials. Please check your .env file.")

# Initialize PayOS SDK instance
payos = PayOS(client_id, api_key, checksum_key)

# ----------------------------------------------------------------------
# Initialize FastAPI application with custom API docs URLs
# ----------------------------------------------------------------------
app = FastAPI(
    title="PayOS Dynamic QR Payment API",
    description="Easily integrate dynamic QR code payments via PayOS",
    version="1.0.0",
    docs_url="/api/py/docs",
    openapi_url="/api/py/openapi.json",
)

# ----------------------------------------------------------------------
# CORS Configuration - Allow frontend or other clients to access API
# ----------------------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You may restrict this to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------------------------------------------------
# Default return URL (frontend will handle redirect after success/failure)
# ----------------------------------------------------------------------
YOUR_DOMAIN = os.getenv("CLIENT_DOMAIN", "http://localhost:3000/payment")

# ----------------------------------------------------------------------
# Health Check / Test Route
# ----------------------------------------------------------------------


@app.get("/api/py/helloFastApi")
def hello_fast_api():
    return {"message": "Hello from FastAPI"}

# ----------------------------------------------------------------------
# Pydantic Models for Request Validation
# ----------------------------------------------------------------------


class ItemInput(BaseModel):
    name: str = "Item Name"
    quantity: int = 1
    price: int = 2000


class CreatePaymentRequest(BaseModel):
    description: str = "Order description"
    items: List[ItemInput]
    buyer_name: Optional[str] = "Nguyen Van A"
    buyer_email: Optional[str] = "nguyenvana@example.com"
    buyer_phone: Optional[str] = "0123456789"

# ----------------------------------------------------------------------
# API Endpoint: Create a dynamic QR payment link via PayOS
# ----------------------------------------------------------------------


@app.post("/api/py/create-payment-link")
async def create_payment_link(request: CreatePaymentRequest):
    """
    Generate a secure payment link using PayOS that includes
    dynamic QR code for real-time payment.

    Returns:
        A JSON response containing the checkout URL.
    """
    try:
        # Map item input to PayOS's item format
        items = [
            ItemData(name=item.name, quantity=item.quantity, price=item.price)
            for item in request.items
        ]

        # Calculate total amount to be paid
        total_amount = sum(item.price * item.quantity for item in request.items)

        # Use current timestamp as unique order code (you can improve this)
        order_code = int(time.time())

        # Construct the payment request payload
        payment_data = PaymentData(
            orderCode=order_code,
            amount=total_amount,
            description=request.description,
            items=items,
            cancelUrl=f"{YOUR_DOMAIN}?canceled=true&orderCode={order_code}",
            returnUrl=f"{YOUR_DOMAIN}?success=true&orderCode={order_code}",
            buyerName=request.buyer_name,
            buyerEmail=request.buyer_email,
            buyerPhone=request.buyer_phone,
            expiredAt=int(time.time()) + 600  # Link valid for 10 minutes
        )

        # Create payment link via PayOS
        payment_link_response = payos.createPaymentLink(payment_data)

        return JSONResponse(content={"checkoutUrl": payment_link_response.checkoutUrl})

    except Exception as e:
        return JSONResponse(content={"detail": str(e)}, status_code=500)
