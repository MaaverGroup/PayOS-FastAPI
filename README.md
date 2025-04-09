# PayOS-FastAPI
Hệ thống backend FastAPI sẵn sàng triển khai, tích hợp với PayOS để tạo các liên kết thanh toán QR code động. Được xây dựng đặc biệt để có thể triển khai thông qua Vercel và tích hợp liền mạch với Next.js 15.2 App Router.

## Tổng quan
PayOS-FastAPI cung cấp dịch vụ backend nhẹ nhưng mạnh mẽ, cho phép ứng dụng của bạn tạo các liên kết thanh toán theo yêu cầu. Nó xử lý tất cả các phức tạp của tích hợp PayOS, cấu hình CORS và thiết lập dựa trên môi trường để bạn có thể tập trung vào việc xây dựng ứng dụng của mình.

## Tính năng
-   💰 Tạo yêu cầu thanh toán động thông qua API
-   🔗 Tạo liên kết thanh toán sử dụng PayOS
-   🔒 Thiết lập CORS đầy đủ ngay từ đầu
-   ⚙️ Cấu hình dựa trên môi trường thông qua tệp `.env`
-   📚 Tài liệu API tự động thông qua Swagger UI tại `/api/py/docs`
-   🚀 Được tối ưu hóa cho việc triển khai Vercel
-   ⚡ Hỗ trợ hoàn hảo cho ứng dụng Next.js 15.2 App Router

## Hướng dẫn thiết lập
### Yêu cầu
-   Node.js (v16+)
-   Python (v3.8+)
-   Tài khoản PayOS với thông tin xác thực API

### Cài đặt
1. Sao chép repository:
    ```bash
    git clone https://github.com/MaaverGroup/PayOS-FastAPI.git
    cd PayOS-FastAPI
    ```
2. Thiết lập môi trường ảo Python:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Trên Windows: venv\Scripts\activate
    ```
3. Cài đặt các gói phụ thuộc Python:
    ```bash
    pip install -r requirements.txt
    ```
4. Cài đặt các gói phụ thuộc Node.js:
    ```bash
    npm install
    # hoặc
    yarn install
    ```
5. Sao chép `.env.example` để tạo tệp `.env` của riêng bạn:
    ```bash
    cp .env.example .env
    ```
6. Cập nhật tệp `.env` với thông tin xác thực PayOS của bạn:
    ```
    PAYOS_CLIENT_ID=your_client_id
    PAYOS_API_KEY=your_api_key
    PAYOS_CHECKSUM_KEY=your_checksum_key
    CLIENT_DOMAIN=http://localhost:3000/payment
    ```

### Chạy máy chủ
Khởi động máy chủ phát triển:
```bash
npm run dev
# hoặc
yarn dev
```
API của bạn sẽ có sẵn tại `http://localhost:3000/api/py` với tài liệu Swagger tại `http://localhost:3000/api/py/docs`.

## Triển khai
Dự án này được thiết kế để triển khai trực tiếp lên Vercel:
1. Đẩy repository của bạn lên GitHub
2. Kết nối repository với Vercel
3. Cấu hình các biến môi trường trong bảng điều khiển Vercel
4. Triển khai!

## Sử dụng API
### Kiểm tra trạng thái
Bạn có thể xác minh API đang hoạt động với một yêu cầu GET đơn giản:
```bash
curl https://your-vercel-deployment.vercel.app/api/py/helloFastApi
```
Phản hồi:
```json
{
    "message": "Hello from FastAPI"
}
```

### Tạo liên kết thanh toán
Tạo liên kết thanh toán với yêu cầu POST sau:
```javascript
// Ví dụ phía máy khách sử dụng fetch API
const response = await fetch("https://your-vercel-deployment.vercel.app/api/py/create-payment-link", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify({
        description: "Đơn hàng áo thun và quần jean",
        items: [
            {
                name: "Áo thun",
                quantity: 1,
                price: 100000,
            },
            {
                name: "Quần jean",
                quantity: 1,
                price: 200000,
            },
        ],
        buyer_name: "Nguyễn Văn A",
        buyer_email: "nguyen.van.a@example.com",
        buyer_phone: "0987654321",
    }),
});
const data = await response.json();
const checkoutUrl = data.checkoutUrl;
// Chuyển hướng người dùng đến checkoutUrl để thanh toán
window.location.href = checkoutUrl;
```
Phản hồi:
```json
{
    "checkoutUrl": "https://pay.payos.vn/web/xxxxxxxxx"
}
```
Trang thanh toán PayOS sẽ xử lý quy trình thanh toán và chuyển hướng người dùng trở lại URL trả về được chỉ định của bạn sau đó.

Để xem tài liệu API đầy đủ, hãy truy cập Swagger UI tại `/api/py/docs`.

## Đóng góp
Chúng tôi hoan nghênh mọi đóng góp! Vui lòng gửi Pull Request.

## Giấy phép
Dự án này là mã nguồn mở và có sẵn theo [Giấy phép MIT](LICENSE).

## Ghi công
Được xây dựng và duy trì với ❤️ bởi [Maaver Group 🇻🇳](https://maaver.com)

---

# PayOS-FastAPI (English)
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
