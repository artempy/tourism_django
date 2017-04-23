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

var loading = false;
$(window).scroll(function(){
if((($(window).scrollTop()+$(window).height())+250)>=$(document).height()){
  if(loading == false){
  loading = true;
  $('#loadingbar').css("display","block");
  $.get("load.php?start="+$('#loaded_max').val(), function(loaded){
    $('body').append(loaded);
    $('#loaded_max').val(parseInt($('#loaded_max').val())+50);
    $('#loadingbar').css("display","none");
    loading = false;
  });
  }
}
});
$(document).ready(function() {
$('#loaded_max').val(50);
});
