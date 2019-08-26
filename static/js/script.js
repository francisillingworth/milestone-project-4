$(document).ready(function() {
    $(".view_comments").click(function() {
        var $this = $(this);
        var index = $this.data("index");
        $("#comments-" + index).toggle('1000');
    });
});

$('.see_less').click(function() {
    var $this = $(this);
    $this.toggleClass('see_less');
    if ($this.hasClass('see_less')) {
        $this.text('View Comments');
    }
    else {
        $this.text('Hide Comments');
    }
});


