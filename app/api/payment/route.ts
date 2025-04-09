/**
 * ───────────────────────────────────────────────────────────────
 * 🚀 Project: PayOS-FastAPI – FastAPI Serverless on Vercel
 * 🔗 GitHub: https://github.com/MaaverGroup/PayOS-FastAPI
 * 🧑‍💻 Author: Maaver Group
 * 🌐 Website: https://maaver.com
 * 📄 License: MIT
 * 📅 Created: 2025-04-09
 * ───────────────────────────────────────────────────────────────
 *
 * Description:
 * This file acts as a proxy route from the Next.js frontend
 * to the FastAPI backend (deployed serverlessly on Vercel),
 * handling QR code payment link creation via PayOS.
 */

import { NextRequest, NextResponse } from "next/server";

/**
 * POST /api/create-payment-link
 *
 * This API route proxies payment creation requests from the frontend
 * to a FastAPI backend that communicates with the PayOS service.
 *
 * If BACKEND_URL is not set in the environment, it defaults to http://localhost:8000
 * for development use.
 */
export async function POST(req: NextRequest): Promise<NextResponse> {
    try {
        // Parse the request body
        const body = await req.json();

        // Use environment variable or fallback to localhost
        const backendBaseUrl = process.env.BACKEND_URL || "http://localhost:8000/api/py";

        // Construct the full backend endpoint URL
        const backendUrl = `${backendBaseUrl}/create-payment-link`;

        // Forward the request to the backend
        const response = await fetch(backendUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(body),
        });

        const data = await response.json();

        // Success: Return the checkout URL
        if (response.ok && data.checkoutUrl) {
            return NextResponse.json({ checkoutUrl: data.checkoutUrl });
        }

        // Handle error returned from backend
        return NextResponse.json(
            {
                error: data?.detail || "Failed to create payment link. No checkout URL returned.",
            },
            {
                status: response.status || 400,
            }
        );
    } catch (err) {
        // Catch unexpected errors
        const message = err instanceof Error ? err.message : "Unexpected server error";
        return NextResponse.json({ error: message }, { status: 500 });
    }
}
