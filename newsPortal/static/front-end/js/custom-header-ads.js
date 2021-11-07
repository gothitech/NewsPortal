// custom ads section at header
const custom_header_ads_section = document.querySelector('.section-for-custom-ads');
const close_custom_header_ads_btn   = document.querySelector('.close_custom_header_ads');

const close_custom_header_ads = (element) =>{
    element.style.display = 'none';
}

close_custom_header_ads_btn.onclick =() =>{
    close_custom_header_ads(custom_header_ads_section);
}

// section for ads at middle
const section_for_ads = document.querySelector('.section-for-add');
const close_section_for_ads_btn = document.querySelector('.close_section_for_ads_btn');

