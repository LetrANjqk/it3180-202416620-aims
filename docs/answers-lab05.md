# Lab 05 - Câu hỏi thảo luận

**1. Ưu, nhược điểm của upstream first so với release first?**
- **Upstream first (Microsoft - Sửa trên master rồi mang về release):** 
  + Ưu điểm: Đảm bảo bản vá luôn có mặt trên phiên bản tương lai, không bao giờ bị quên. 
  + Nhược điểm: Nếu master đã thay đổi quá nhiều so với bản release, việc cherry-pick ngược về sẽ rất khó và sinh xung đột.
- **Release first (Học phần - Sửa trên release rồi mang lên master):**
  + Ưu điểm: Fix lỗi nhanh chóng, dễ dàng và an toàn trực tiếp cho bản release đang lỗi.
  + Nhược điểm: Dễ quên việc lan truyền (backport) lên master, khiến lỗi bị tái diễn ở phiên bản sau.

**2. Nếu quên lan truyền bản sửa sang release/lab05, lệnh nào ở Phần F sẽ phát hiện?**
Lệnh `git cherry -v origin/master origin/release/lab05` hoặc lệnh `git tag --contains <FIX_SHA>`. 
Ngoài ra, đoạn script kiểm tra Python vòng lặp `for ref in v1.0.1 v1.1.0 master...` cũng sẽ phát hiện vì ở phiên bản `v1.1.0` sẽ in ra danh sách trống `[]` thay vì in ra `1`.