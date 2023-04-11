

  var swiper = new Swiper(".mySwiper", {
    slidesPerView: 5,
    slidesPerColumn: 10,
    spaceBetween: 30,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
      },
    keyboard: {
      enabled: true,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },

    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    breakpoints: {
        360: {
            slidesPerView: 2,
            spaceBetween: 10,
            allowTouchMove:true,
        },
        768: {
            slidesPerView: 3,
            spaceBetween: 20,
            allowTouchMove:true,
        },
        1000: {
            slidesPerView: 4,
            spaceBetween: 20,
            allowTouchMove:true,
        },
        1200: {
            slidesPerView: 5,
            spaceBetween: 20,
            allowTouchMove:true,
        }
  }});
  var swiper = new Swiper(".SwiperPopular", {
    slidesPerView: 5,
    slidesPerColumn: 10,
    spaceBetween: 30,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
      },
    keyboard: {
      enabled: true,
    },
    pagination: {
      el: ".swiper-pagination2",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    breakpoints: {
        360: {
            slidesPerView: 2,
            spaceBetween: 10,
            allowTouchMove:true,
        },
        768: {
            slidesPerView: 3,
            spaceBetween: 20,
            allowTouchMove:true,
        },
        1000: {
            slidesPerView: 4,
            spaceBetween: 20,
            allowTouchMove:true,
        },
        1200: {
            slidesPerView: 5,
            spaceBetween: 20,
            allowTouchMove:true,
        }
  }});
       