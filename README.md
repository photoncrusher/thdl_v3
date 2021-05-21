# TÍCH HỢP DỮ LIỆU BẢN FINAL
Đây là project tích hợp dữ liệu các sản phẩm từ Apple. Thậm chí có thể tích hợp hết các sản phẩm công nghệ
## MÔ TẢ PROJECT
- thư mục spider: chứa các spider. Để tích hợp vào hệ thống, sau khi crawl, khi yield cần để data đã yield trong convert(). VD: yield data chuyển thành yield convert(data)
- matching.py: chứa các khoảng cách, công thức liên quan đến schema matching, string matching. Ở đây ta dùng Fuzzy matching đã học trên lớp (còn gọi khoảng cách levenshtein). Không nên thực hiện thay đổi code ở đây.
- data_filling.py: chứa các công thức/ hàm liên quan đến data matching và data filling. Hiện giờ công thức của chúng ta mới chỉ phủ thuộc vào name. Công thức kỳ vọng sẽ gồm cả name, storage,cpu,ram tuy nhiên dữ liệu gặp vấn đề khi các trường đó thiếu khá nhiều hoặc khá lệch nhau do chưa regex.Ở đây ko sử dụng học máy mà sử dụng khoảng cách Jaccard. (nên sửa code/ công thức ở đoạn này)
- csv_to_elastic.py: file để chuyển dữ liệu từ csv sang elastic search. Tuy nhiên chưa chạy được vì gặp 1 vấn đề: khi cần chuyển thì tất cả dữ liệu ko dc isnan(). Nói cách khác, trước khi chuyển phải cho dữ liệu đó thành trường string 'unknow' hết.(cái này EZ).
- data.csv: file cuối cùng trước khi vào elastic
- t1a.csv: file chuẩn của Quang Phúc
- CHÚ Ý!!! hiện tại sau khi crawl xong cần tự vào file json format, sau đó chuyển json thành csv trước khi thực hiện các bước tiếp theo

## CÁCH CHẠY
- Kiểm tra, đổi đường dẫn trong các file  py
- .\run_crawler.sh và nó sẽ tự crawl, chuyển đổi và đẩy dữ liệu lên elastic search (EZ)
- Tuy nhiên hiện tại nếu chạy run_crawler.sh thì sẽ chỉ crawl data về và đưa vào macbook.json(file tổng đã qua string nhưng chưa qua data matching) => cần fix ngay (sẽ nói rõ ở dưới)

## TỔNG KẾT CÁC PROBLEM CẦN FIX NGAY:
### Quan trọng:
- Crawl ngay 1 bản mẫu (đầy đủ) của iphone, ipad và applewatch để data matching.
- Dữ liệu quá ít, cần crawl trên shopee, lazada ngay Ipad và Iphone (crawl 2 trường name và price, sau đó yield convert(data) và nó sẽ match vào csdl 1 cách magic).
- <strike> fix file macbook.json định dạng ko đúng do crawl đổ vào nhiều lần (chuyển \]\[ thành dấu ,) => chính là cái lỗi gây ra cho run.sh nè </strike>
- Ông @QuangPhuc kiểm tra lại cái crawler xem, khá nhiều sản phẩm ở 1 trang của ông bị thiếu trường name ! (cái này thiếu name thì match ko nổi).
- chuyển các trường nan về thành string 'unknow' trước khi đẩy vào elastic search
- Ông Quân check ngay cho ae cái kibana nhé. Tôi sẽ không đụng đến phần đấy đâu. file csv của ông là data.csv
- Làm cái công thức khác về data matching.
