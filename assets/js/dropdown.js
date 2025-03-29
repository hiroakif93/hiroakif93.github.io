
document.addEventListener('DOMContentLoaded', function() {
    var dropdowns = document.querySelectorAll('nav > ul > li');

    dropdowns.forEach(function(dropdown) {
        dropdown.addEventListener('click', function() {
            var openDropdown = document.querySelector('nav .show');
            if (openDropdown && openDropdown !== dropdown) {
                openDropdown.classList.remove('show');
            }
            dropdown.classList.toggle('show');
        });
    });

    // ドキュメント内のどこかをクリックしたときにドロップダウンを閉じる
    document.addEventListener('click', function(e) {
        if (!e.target.closest('nav')) {
            document.querySelectorAll('nav .show').forEach(function(openDropdown) {
                openDropdown.classList.remove('show');
            });
        }
    });
});
