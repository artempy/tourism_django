jQuery(document).ready(function(){
//search box
    var tl_keyword='Поиск на сайте...';
    jQuery(".mainsearch .keyword").val(tl_keyword);

    jQuery(".mainsearch").hover(
        function () {
            //jQuery(".mainsearch .keyword").css('visibility', 'visible');
            jQuery(this).addClass("mainsearch_hover");
        },
        function () {
            if(jQuery(".mainsearch .keyword").val()==tl_keyword){
                //jQuery(".mainsearch .keyword").css('visibility', 'hidden');
                jQuery(this).removeClass("mainsearch_hover");
            }
    });
    jQuery(".mainsearch .keyword").bind("focus", function(){
        if(jQuery(this).val()==tl_keyword) jQuery(this).val('');
    });

    jQuery(".mainsearch .keyword").bind("blur", function(){
        if(jQuery(this).val()==''){
            jQuery(this).val(tl_keyword);
            //jQuery(this).css('visibility', 'hidden');
            jQuery(".mainsearch").removeClass("mainsearch_hover");
        }
    });


//drop-down menu
    jQuery("div.menu ul ul li:has(ul)").find("a:first").append(" &raquo;");

//prepare of non-widget sidebar (may cause adsense problem, please use widget for sidebar better)
    jQuery("#sidebar1>ul>li").not(":has('div.sb1_block_top')").wrapInner('<div class="sb1_block_top"></div>');
    jQuery("#sidebar1>ul>li>div.sb1_block_top").not(":has('div.sb1_block_btm')").wrapInner('<div class="sb1_block_btm"></div>');
    for(var tm_count=1;tm_count<=5;tm_count++){
        jQuery(".menu>ul>li:nth-child("+tm_count+")>a").after('<div class="menu_icon'+tm_count+'"></div>');
    }
//resize
    jQuery(window).resize();
});
jQuery(window).resize(
function(){
    if(jQuery("#bg_top").width()%2 ==1){
        jQuery("#bg_top").css("margin-left","-1px");
    }else{
        jQuery("#bg_top").css("margin-left","0px");
    };
});

$(document).ready(function() {
    $('#loaded_max').val(50);
    $("i#reply_comment").click(function() {
        var author = $('h6', $(this).parent()).html();
        $("textarea#id_text").val(author + ', ');
        $("textarea#id_text").focus();
    });
});

$(document).ready(function(e) {
 var a = 300,
 t = 1200,
 l = 700,
 s = e(".cd-top");
 e(window).scroll(function() {
 e(this).scrollTop() > a ? s.addClass("cd-is-visible") : s.removeClass("cd-is-visible cd-fade-out"), e(this).scrollTop() > t && s.addClass("cd-fade-out")
 }), s.on("click", function(a) {
 a.preventDefault(), e("body,html").animate({
 scrollTop: 0
 }, l)
 })
})
