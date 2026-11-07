# Lab 02 - Câu hỏi thảo luận

**1. Vì sao phải đồng bộ master trước khi PR?**
Để đảm bảo nhánh tính năng của bạn tích hợp tốt với mã nguồn mới nhất. Việc đồng bộ giúp phát hiện và giải quyết xung đột (conflict) ngay trên nhánh cục bộ trước khi đưa lên PR, đảm bảo PR luôn trong trạng thái có thể tự động merge.

**2. Khi nào không được rebase?**
Không bao giờ được rebase các commit đã được push lên máy chủ (remote) và chia sẻ cho người khác. Rebase viết lại lịch sử commit, làm thay đổi mã SHA, sẽ gây ra lỗi đồng bộ nghiêm trọng cho những người đang cùng làm việc trên nhánh đó.

**3. feature/* khác topic/* ra sao?**
- `feature/*` dùng để phát triển các tính năng phần mềm, làm thay đổi mã nguồn ứng dụng (ví dụ: code chức năng in giỏ hàng).
- `topic/*` dùng cho các chủ đề công việc không liên quan trực tiếp đến logic phần mềm như cập nhật tài liệu, thiết lập cấu hình CI/CD, thêm PR template.