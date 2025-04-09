# PayOS-FastAPI

A ready-to-deploy FastAPI backend that integrates with PayOS to generate dynamic QR code payment links. Built specifically to be deployable via Vercel and integrate seamlessly with Next.js 15.2 App Router.

## Overview

PayOS-FastAPI provides a lightweight yet powerful backend service that enables your application to generate payment links on demand. It handles all the complexities of PayOS integration, CORS configuration, and environment-based setup so you can focus on building your application.

## Features

-   💰 Dynamic payment request generation via API
-   🔗 Payment link generation using PayOS
-   🔒 Complete CORS setup out of the box
-   ⚙️ Environment-based configuration via `.env`
-   📚 Automatic API documentation via Swagger UI at `/api/py/docs`
-   🚀 Optimized for Vercel deployment
-   ⚡ Perfect companion for Next.js 15.2 App Router applications

## Setup Guide

### Prerequisites

-   Node.js (v16+)
-   Python (v3.8+)
-   PayOS account with API credentials

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/MaaverGroup/PayOS-FastAPI.git
    cd PayOS-FastAPI
    ```

2. Set up Python virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Install Node.js dependencies:

    ```bash
    npm install
    # or
    yarn install
    ```

5. Copy `.env.example` to create your own `.env` file:

    ```bash
    cp .env.example .env
    ```

6. Update the `.env` file with your PayOS credentials:
    ```
    PAYOS_CLIENT_ID=your_client_id
    PAYOS_API_KEY=your_api_key
    PAYOS_CHECKSUM_KEY=your_checksum_key
    CLIENT_DOMAIN=http://localhost:3000/payment
    ```

### Running the Server

Start the development server:

```bash
npm run dev
# or
yarn dev
```

Your API will be available at `http://localhost:3000/api/py` with Swagger documentation at `http://localhost:3000/api/py/docs`.

## Deployment

This project is designed to be deployed directly to Vercel:

1. Push your repository to GitHub
2. Connect the repository to Vercel
3. Configure environment variables in Vercel dashboard
4. Deploy!

## API Usage

### Health Check

You can verify the API is working with a simple GET request:

```bash
curl https://your-vercel-deployment.vercel.app/api/py/helloFastApi
```

Response:

```json
{
    "message": "Hello from FastAPI"
}
```

### Creating Payment Links

Generate a payment link with the following POST request:

```javascript
// Client-side example using fetch API
const response = await fetch("https://your-vercel-deployment.vercel.app/api/py/create-payment-link", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify({
        description: "Order for T-shirt and Jeans",
        items: [
            {
                name: "T-shirt",
                quantity: 1,
                price: 100000,
            },
            {
                name: "Jeans",
                quantity: 1,
                price: 200000,
            },
        ],
        buyer_name: "John Doe",
        buyer_email: "john.doe@example.com",
        buyer_phone: "0987654321",
    }),
});

const data = await response.json();
const checkoutUrl = data.checkoutUrl;
// Redirect user to checkoutUrl for payment
window.location.href = checkoutUrl;
```

Response:

```json
{
    "checkoutUrl": "https://pay.payos.vn/web/xxxxxxxxx"
}
```

The PayOS checkout page will handle the payment process and redirect the user back to your specified return URL afterward.

For complete API documentation, visit the Swagger UI at `/api/py/docs`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Credits

Built and maintained with ❤️ by [Maaver Group 🇻🇳](https://maaver.com)
