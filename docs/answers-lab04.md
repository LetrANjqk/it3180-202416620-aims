# Lab 04 - Câu hỏi thảo luận

**1. Vì sao release/* không merge vào master? So sánh với GitFlow.**
Theo Release Flow của bài thực hành, nhánh `release/*` là nhánh duy trì vĩnh viễn (đóng băng) cho một phiên bản, mã nguồn (kể cả hotfix) không bao giờ được merge ngược lại `master`. 
(Trong GitFlow, nhánh release chỉ là tạm thời, sau khi phát hành xong sẽ được merge vào cả `main` và `develop` rồi bị xóa).

**2. Vì sao lên 1.0.0 mà không phải 0.4.0?**
Theo nguyên tắc Semantic Versioning, phiên bản `0.x.y` dành cho giai đoạn phát triển ban đầu. Việc nhảy số lên bản MAJOR `1.0.0` đánh dấu dự án đã đạt trạng thái ổn định, hoàn thiện các tính năng cốt lõi và sẵn sàng phát hành chính thức để sử dụng.