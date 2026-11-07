# Lab 03 - Câu hỏi thảo luận

**1. Merge base là gì?**
Merge base là commit tổ tiên chung (common ancestor) gần nhất của hai nhánh đang được merge. Git sử dụng nó làm điểm tham chiếu chuẩn để phân tích sự khác biệt của cả hai nhánh nhằm tính toán cách gộp mã nguồn lại với nhau.

**2. Vì sao master/release/* phải dùng revert?**
`master` và `release/*` là các nhánh dùng chung, đã được chia sẻ công khai và chứa các baseline. Dùng `revert` sẽ tạo ra một commit mới để đảo ngược thay đổi mà không làm thay đổi lịch sử cũ, không phá vỡ cấu trúc và mã băm SHA của các commit đã có. (Trái ngược với `reset` làm mất lịch sử).