import re
with open('html/dance.html', 'r', encoding='utf-8') as f:
    text = f.read()

script_new = '''<script>
        $(document).ready(function() {
            var modal = $('#img-modal');
            var modalImg = $('#modal-img');
            var galleryImgs = $('.gallery img');

            galleryImgs.each(function() {
                var img = $(this);
                img.click(function() {
                    modalImg.attr('src', img.attr('src'));
                    modal.addClass('show');
                });
            });

            modal.click(function() {
                modal.removeClass('show');
                setTimeout(function() {
                    modalImg.attr('src', "");
                }, 300);
            });

            var chartDom = $('#echarts-dance')[0];
            if (chartDom) {
                var myChart = echarts.init(chartDom);'''

text = re.sub(r'<script>\s*document\.addEventListener[^<]*?var myChart = echarts\.init\(chartDom\);', script_new, text)

with open('html/dance.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Fixed dance.html')
