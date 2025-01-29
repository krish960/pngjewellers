document.addEventListener('DOMContentLoaded', function () {

  const accountLink = document.getElementById('accountLink');
  const accountPopup = document.querySelector('.account-popup');


  accountLink.addEventListener('click', function (event) {
    event.preventDefault();
    accountPopup.classList.toggle('d-none');
  });


  document.addEventListener('click', function (event) {
    if (!accountLink.contains(event.target) && !accountPopup.contains(event.target)) {
      accountPopup.classList.add('d-none');
    }
  });
});

//navbar  diamond section 

document.querySelectorAll('[data-category]').forEach(item => {
  item.addEventListener('click', function (event) {
    event.preventDefault();

    const category = event.target.getAttribute('data-category');

    const styleContent = document.getElementById('styleContent').querySelector('ul');
    const typeContent = document.getElementById('typeContent').querySelector('ul');

    let categoryStyleContent = '';
    let categoryTypeContent = '';


    switch (category) {
      case 'earrings':
        categoryStyleContent = `
          <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/Diamond-Earring-studspng__9289701641419091501.webp" alt="" style="width: 13%;">   <a href="/studs" style="text-decoration: none;color:black">Studs</a></li>
          <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/Diamond-Earring-Hoops-amp-Huggiespng__1180141710801056052.webp" alt="" style="width: 13%;"> <a href="/HoopsandHuggies" style="text-decoration: none;color:black"> Hoops and Huggies</a></li>
          <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/Diamond-Earring-Drops-amp-Danglerspng__12034144971548127278.webp" alt="" style="width: 13%;"> <a href="/DropsandDangless" style="text-decoration: none;color:black"> Drops and Danglers</a></li>
          <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/sui-dhagapng__1944820994949121427.webp" alt="" style="width: 13%;"> <a href="/sui_daga" style="text-decoration: none;color:black"> Sui Dhaga</a></li>
        `;
        break;
      case 'rings':
        categoryStyleContent = `
          <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/Diamond-RIng-Bandspng__559985761228907293.webp" alt="" style="width: 13%;"><a href="/Diamondrings_bands" style="text-decoration: none;color:black">Bands</a></li>
          <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/Diamond-RIng-Engagement-Ringspng__21050513291752491175.webp" alt="" style="width: 13%;"><a href="/Diamond_engagement_rings" style="text-decoration: none;color:black"> Engagement Rings</a></li>
      
           <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/Diamond-RIng-Engagement-Ringspng__21050513291752491175.webp" alt="" style="width: 13%;"><a href="/Dai_Fashion_Ring" style="text-decoration: none;color:black">Fashion Ring</a></li>
           <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/Diamond-RIng-Engagement-Ringspng__21050513291752491175.webp" alt="" style="width: 13%;"><a href="/Diamond_casual_rings" style="text-decoration: none;color:black">casual rings</a></li>

        `;
        break;
      case 'necklaces':
        categoryStyleContent = `
          <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/Diamond-Lariat-Necklacepng__70677273822617497.webp" alt="" style="width: 13%;"><a href="/DimondNecklasLarient" style="text-decoration: none;color:black">  Lariat Necklace</a></li>
          <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/Short-necklacemenu-itemspng__19878403781415637627.webp" alt="" style="width: 13%;"> <a href="/Diamond_short_necklaces" style="text-decoration: none;color:black">Diamond -Short Necklace</a></li>
            
        `;
        break;
      case 'pendant':
        categoryStyleContent = `
          <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/catalog/product/preview/F4D6ZG/DIDP0024-FXY48-main.webp" alt="" style="width: 13%;"><a href="/Diamond_hearte_pendant" style="text-decoration: none;color:black"> Heart Pendant</a></li>
            <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/catalog/product/preview/F4D6ZG/DIDP0024-FXY48-main.webp" alt="" style="width: 13%;"><a href="/Diamond_religious_pendant" style="text-decoration: none;color:black">diamond religious pendant</a></li>
        `;
        break;
      case 'mangalsutra':
        categoryStyleContent = `
          <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/catalog/product/preview/F4D6ZG/GMM21-FXY20-main.webp" alt="" style="width: 13%;"><a href="/studs" style="text-decoration: none;color:black">  Diamond Mangalsutra</a></li>
          <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/Diamond-Trendy-Modern-Mangalsutrapng__1846948015552973868.webp" alt="" style="width: 13%;"><a href="/Trendy_mo_d_mangalsutra" style="text-decoration: none;color:black"> Trendy Mordern Mangalsutra</a></li>
         `;
        break;
      case 'bracelets':
        categoryStyleContent = `
          <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/diamonddd5-copypng__16325653871911890045.webp" alt="" style="width: 13%;"><a href="/Bangles_Flexible_Bracel" style="text-decoration: none;color:black">Flexible Bracelet</a></li>
        `;
        break;
      case 'kurta-button':
        categoryStyleContent = `
          <li><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnb0k24qkYVtNW7jxVkWT5ip5O4X1kqt__BQ&s" alt="" style="width: 13%;"><a href="/Diamond_kurta_buttons" style="text-decoration: none;color:black"> Kurta Button</a></li>
        `;
        break;
      case 'cufflinks':
        categoryStyleContent = `
          <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/Diamond-Cufflinkpng__1871927811916682737.webp" alt="" style="width: 13%;"><a href="/Diamond_cufflink" style="text-decoration: none;color:black"> Diamond Cufflinks</a></li>
        `;
        break;
      case 'nosepin':
        categoryStyleContent = `
          <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/Diamond-Nosepinpng__701874338197114867.webp" alt="" style="width: 13%;"> <a href="/Diamond_nosepin" style="text-decoration: none;color:black">diamond nosepin</a></li>
        `;
        break;
      default:
        categoryStyleContent = `<li>No items available for this category</li>`;
    }


    styleContent.innerHTML = categoryStyleContent;


    switch (category) {
      case 'earrings':
        categoryTypeContent = `
          <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/Partywear-01png__994808381.png" alt="" style="width: 13%;"><a href="/Diamond_partyWear" style="text-decoration: none;color:black">Party Wear</a></li>
          <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/Office-Wear-01png__56898861.png" alt="" style="width: 13%;"> Office Wear</li>
          <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/Dailywear-01png__106309190.png" alt="" style="width: 13%;"><a href="/Daily_wear" style="text-decoration: none;color:black"> Daily Wear</a></li>
        `;
        break;
      case 'rings':
        categoryTypeContent = `
          <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/Partywear-01png__994808381.png" alt="" style="width: 13%;"><a href="/Diamond_partyWear" style="text-decoration: none;color:black">Party Wear</a></li>
          <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/Office-Wear-01png__56898861.png" alt="" style="width: 13%;"> Office Wear</li>
          <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/Dailywear-01png__106309190.png" alt="" style="width: 13%;"><a href="/Daily_wear" style="text-decoration: none;color:black">Daily Wear</a></li>
        `;
        break;

      default:
        categoryTypeContent = `<li>No items available for this category</li>`;
    }


    typeContent.innerHTML = categoryTypeContent;
  });
});

// Gold js 
document.querySelectorAll('[data-category]').forEach(item => {
  item.addEventListener('click', function (event) {
    event.preventDefault();
    const category = event.target.getAttribute('data-category');

    const styleContent = document.getElementById('shopByStyle').querySelector('ul');
    const typeContent = document.getElementById('shopByType').querySelector('ul');

    let categoryShopByStyle = '';
    let categoryShopByType = '';

    switch (category) {
      case 'gold-rings':
        categoryShopByStyle = `
            <li><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgldtyqY1WE-00F98zktc3Zc1qGASrR3Vwbw&s" alt="Hoops and Huggies" class="menu-icon" style="width: 20%; > <a href="#" class="menu-link">casual ring</a></li>
            <li><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgldtyqY1WE-00F98zktc3Zc1qGASrR3Vwbw&s" alt="Drops and Danglers" class="menu-icon" style="width: 20%; > <a href="/studs" class="menu-link">traditional ring</a></li>
            <li><img src=https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgldtyqY1WE-00F98zktc3Zc1qGASrR3Vwbw&s" alt="Sui Dhaga" class="menu-icon" style="width: 20%; > <a href="/studs" class="menu-link">casual ring</a></li>
          `;
        categoryShopByType = `
                    <li><a href="/GoldParty_wear" class="menu-link">Party ware</a></li>
                    <li><a href="/office_wear" class="menu-link">office ware</a></li>
                    <li><a href="/Gold_daily_wear" class="menu-link">daily wear</a></li>
                    <li><a href="/Gold_kids_earrings" class="menu-link">Kids</a></li>
                    <li><a href="/Goldrops_and_danglers" class="menu-link">Drops and Danglers</a></li>
                  `;
        break;
      case 'gold-chain':
        categoryShopByStyle = `
                <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/Diamond-Earring-studspng__9289701641419091501.webp" alt="Studs" class="menu-icon" > <a href="/studs" class="menu-link">Studs</a></li>
                <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/Diamond-Earring-Hoops-amp-Huggiespng__1180141710801056052.webp" alt="Hoops and Huggies" class="menu-icon"> <a href="/studs" class="menu-link">Hoops and Huggies</a></li>
                <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/Diamond-Earring-Drops-amp-Danglerspng__12034144971548127278.webp" alt="Drops and Danglers" class="menu-icon"> <a href="/studs" class="menu-link">Drops and Danglers</a></li>
                <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/sui-dhagapng__1944820994949121427.webp" alt="Sui Dhaga" class="menu-icon"> <a href="/sui_dhaga" class="menu-link">Sui Dhaga</a></li>
              `;
        categoryShopByType = `
                        <li><a href="/layered" class="menu-link">Layered Necklaces</a></li>
                        <li><a href="/simple" class="menu-link">Simple Necklaces</a></li>
                      `;
        break;

      case 'gold-earrings':
        categoryShopByStyle = `
                <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/Hoops-and-Huggiespng__9891364411998204838.webp" alt="Hoops and Huggies" class="menu-icon" style="width: 20%; > <a href="/studs" class="menu-link">casual Earring</a></li>
                <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/Hoops-and-Huggiespng__9891364411998204838.webp" alt="Drops and Danglers" class="menu-icon" style="width: 20%; > <a href="/studs" class="menu-link">traditional Earring</a></li>
                <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/Hoops-and-Huggiespng__9891364411998204838.webp" alt="Sui Dhaga" class="menu-icon" style="width: 20%; > <a href="/studs" class="menu-link">casual Earring</a></li>
                               `;
        categoryShopByType = `
                    <li><a href="/Goldjhumka" class="menu-link">jhumkas</a></li>
                    <li><a href="/mean_studs" class="menu-link">men-studs</a></li>
                  `;
        break;

      case 'gold-bracelets':
        categoryShopByStyle = `
                <li><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbvrWP8w7DOKeNPZk-xMRqytHbujlCSo_tjQ&s" alt="Hoops and Huggies" class="menu-icon" style="width: 20%;" > <a href="/studs" class="menu-link">casual Bracelet</a></li>
                               `;
        categoryShopByType = `
                    <li><a href="/kids_bracelets" class="menu-link">Kids_Bracelets</a></li>
                  `;
        break;

      case 'gold-necklaces':
        categoryShopByStyle = `
                    <li><img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/gold-thusi-1png__3481822581555225449.webp" alt="Pendants" class="menu-icon" style ="width:20%;"> <a href="#" class="menu-link">nacklaces</a></li>
                  `;
        categoryShopByType = `
          
                  `;
        break;





      default:
        categoryShopByStyle = '<li>No items available for this category</li>';
        categoryShopByType = '<li>No items available for this category</li>';
    }


    styleContent.innerHTML = categoryShopByStyle;
    typeContent.innerHTML = categoryShopByType;
  });
});

// bullions

document.querySelectorAll('.dropdown-item').forEach(item => {
  item.addEventListener('click', function (event) {
    const category = event.target.getAttribute('data-category');


    document.getElementById('shopByTypeGold').querySelector('ul').innerHTML = '';

    if (category === 'gold-coin') {

      const typeContent = `
          <li>
            <a href="/Gold_plain">
              <img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/catalog/product/preview/F4D6ZG/GLAX05GM-UXY10-main.webp" alt="Round Gold Coin" style="width: 50px; height: 50px; margin-right: 10px;">Plain
            </a>
          </li>
          <li>
            <a href="/Gold_laxmi_shree">
              <img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/catalog/product/preview/F4D6ZG/GLAX05GM-UXY10-main.webp" alt="Square Gold Coin" style="width: 50px; height: 50px; margin-right: 10px;">Laxmi shree
            </a>
          </li>
          <li>
            <a href="/png">
              <img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/catalog/product/preview/F4D6ZG/GLAX05GM-UXY10-main.webp" alt="Oval Gold Coin" style="width: 50px; height: 50px; margin-right: 10px;">PNG
            </a>
          </li>
        `;
      document.getElementById('shopByTypeGold').querySelector('ul').innerHTML = typeContent;
    } else if (category === 'gold-vedhani') {

      const typeContent = `
          <li>
            <a href="/Gold_vedhani">
              <img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/menus/menu-items/Gold-Vedhanipng__1193883889440908087.webp" alt="Traditional Gold Vedhani" style="width: 50px; height: 50px; margin-right: 10px;">gold vedhani
            </a>
          </li>
          <li>
        `;
      document.getElementById('shopByTypeGold').querySelector('ul').innerHTML = typeContent;
    } else if (category === 'silver-coin') {

      const typeContent = `
          <li>
            <a href="/pure_sliver_chip">
              <img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/catalog/product/preview/F4D6ZG/GPNG10GM-UXU80-main.webp" alt="Round Silver Coin" style="width: 50px; height: 50px; margin-right: 10px;">Pure Silver chip
            </a>
          </li>
          <li>
            <a href="/Trimurtisilver_coins">
              <img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/catalog/product/preview/F4D6ZG/GPNG10GM-UXU80-main.webp" alt="Custom Silver Coin" style="width: 50px; height: 50px; margin-right: 10px;">Trimurti Silver Coins
            </a>
          </li>
          <li>
          <a href="/slive_ganesha_coin">
              <img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/catalog/product/preview/F4D6ZG/GPNG10GM-UXU80-main.webp" alt="Custom Silver Coin" style="width: 50px; height: 50px; margin-right: 10px;">sliver ganesha coin
            </a>
          </li>
          <li>
          <a href="/laxmi_sliver_coin">
              <img src="https://d1put4x3vjlh9s.cloudfront.net/public/uploads/catalog/product/preview/F4D6ZG/GPNG10GM-UXU80-main.webp" alt="Custom Silver Coin" style="width: 50px; height: 50px; margin-right: 10px;"> laxmi silver coin
            </a>
          </li>
        `;
      document.getElementById('shopByTypeGold').querySelector('ul').innerHTML = typeContent;
    }
  });
});
//   main navbar

// vaishnavi bullions subnavbar 

function toggleLike(element) {
  const icon = element.querySelector('i');

  if (icon.classList.contains('far')) {

    icon.classList.remove('far');
    icon.classList.add('fas');
  } else {

    icon.classList.remove('fas');
    icon.classList.add('far');
  }


  element.classList.toggle('liked');


  icon.style.transform = "scale(1.2)";
  setTimeout(() => {
    icon.style.transform = "scale(1)";
  }, 300);
}


function goBack() {
  window.history.back();
}



// dropdowne js

function toggleDropdown(event) {

  document.querySelectorAll('.dropdown-content').forEach((dropdown) => {
    if (dropdown !== event.target.nextElementSibling) {
      dropdown.classList.remove('show');
    }
  });


  const dropdownContent = event.target.nextElementSibling;
  if (dropdownContent) {
    dropdownContent.classList.toggle('show');
  }
}


// index file js
const container = document.getElementById("cardScrollContainer");
const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");

const cardWidth = container.firstElementChild.offsetWidth + 10; // Card width + margin

prevBtn.addEventListener("click", () => {
  container.scrollBy({ left: -cardWidth * 4, behavior: "smooth" }); // Scroll 4 cards left
});

nextBtn.addEventListener("click", () => {
  container.scrollBy({ left: cardWidth * 4, behavior: "smooth" }); // Scroll 4 cards right
});


function toggleLike(element) {
  const icon = element.querySelector('i');

  if (icon.classList.contains('far')) {

    icon.classList.remove('far');
    icon.classList.add('fas');
  } else {

    icon.classList.remove('fas');
    icon.classList.add('far');
  }


  element.classList.toggle('liked');


  icon.style.transform = "scale(1.2)";
  setTimeout(() => {
    icon.style.transform = "scale(1)";
  }, 300);
}


function goBack() {
  window.history.back();
}



// dropdowne js

function toggleDropdown(event) {
  // Close all other dropdowns first
  document.querySelectorAll('.dropdown-content').forEach((dropdown) => {
    if (dropdown !== event.target.nextElementSibling) {
      dropdown.classList.remove('show');
    }
  });

  // Toggle the clicked dropdown
  const dropdownContent = event.target.nextElementSibling;
  if (dropdownContent) {
    dropdownContent.classList.toggle('show');
  }
}



// Hoops and Huggies
function toggleLike(element) {
  const icon = element.querySelector('i');

  if (icon.classList.contains('far')) {

    icon.classList.remove('far');
    icon.classList.add('fas');
  } else {

    icon.classList.remove('fas');
    icon.classList.add('far');
  }


  element.classList.toggle('liked');


  icon.style.transform = "scale(1.2)";
  setTimeout(() => {
    icon.style.transform = "scale(1)";
  }, 300);
}


function goBack() {
  window.history.back();
}



// dropdowne js

function toggleDropdown(event) {
  // Close all other dropdowns first
  document.querySelectorAll('.dropdown-content').forEach((dropdown) => {
    if (dropdown !== event.target.nextElementSibling) {
      dropdown.classList.remove('show');
    }
  });

  // Toggle the clicked dropdown
  const dropdownContent = event.target.nextElementSibling;
  if (dropdownContent) {
    dropdownContent.classList.toggle('show');
  }
}


// Studs

function toggleLike(element) {
  const icon = element.querySelector('i');

  if (icon.classList.contains('far')) {

    icon.classList.remove('far');
    icon.classList.add('fas');
  } else {

    icon.classList.remove('fas');
    icon.classList.add('far');
  }


  element.classList.toggle('liked');


  icon.style.transform = "scale(1.2)";
  setTimeout(() => {
    icon.style.transform = "scale(1)";
  }, 300);
}


function goBack() {
  window.history.back();
}



// dropdowne js

function toggleDropdown(event) {
  // Close all other dropdowns first
  document.querySelectorAll('.dropdown-content').forEach((dropdown) => {
    if (dropdown !== event.target.nextElementSibling) {
      dropdown.classList.remove('show');
    }
  });

  // Toggle the clicked dropdown
  const dropdownContent = event.target.nextElementSibling;
  if (dropdownContent) {
    dropdownContent.classList.toggle('show');
  }
}


function toggleLike(element) {
  const icon = element.querySelector('i');

  if (icon.classList.contains('far')) {

    icon.classList.remove('far');
    icon.classList.add('fas');
  } else {

    icon.classList.remove('fas');
    icon.classList.add('far');
  }


  element.classList.toggle('liked');


  icon.style.transform = "scale(1.2)";
  setTimeout(() => {
    icon.style.transform = "scale(1)";
  }, 300);
}




// dropdowne js

function toggleDropdown(event) {
  // Close all other dropdowns first
  document.querySelectorAll('.dropdown-content').forEach((dropdown) => {
    if (dropdown !== event.target.nextElementSibling) {
      dropdown.classList.remove('show');
    }
  });

  // Toggle the clicked dropdown
  const dropdownContent = event.target.nextElementSibling;
  if (dropdownContent) {
    dropdownContent.classList.toggle('show');
  }
}



function toggleLike(element) {
  const icon = element.querySelector('i');

  if (icon.classList.contains('far')) {

    icon.classList.remove('far');
    icon.classList.add('fas');
  } else {

    icon.classList.remove('fas');
    icon.classList.add('far');
  }


  element.classList.toggle('liked');


  icon.style.transform = "scale(1.2)";
  setTimeout(() => {
    icon.style.transform = "scale(1)";
  }, 300);
}




// dropdowne js

function toggleDropdown(event) {
  // Close all other dropdowns first
  document.querySelectorAll('.dropdown-content').forEach((dropdown) => {
    if (dropdown !== event.target.nextElementSibling) {
      dropdown.classList.remove('show');
    }
  });

  // Toggle the clicked dropdown
  const dropdownContent = event.target.nextElementSibling;
  if (dropdownContent) {
    dropdownContent.classList.toggle('show');
  }
}


function toggleLike(element) {
  const icon = element.querySelector('i');

  if (icon.classList.contains('far')) {

    icon.classList.remove('far');
    icon.classList.add('fas');
  } else {

    icon.classList.remove('fas');
    icon.classList.add('far');
  }


  element.classList.toggle('liked');


  icon.style.transform = "scale(1.2)";
  setTimeout(() => {
    icon.style.transform = "scale(1)";
  }, 300);
}




// dropdowne js

function toggleDropdown(event) {
  // Close all other dropdowns first
  document.querySelectorAll('.dropdown-content').forEach((dropdown) => {
    if (dropdown !== event.target.nextElementSibling) {
      dropdown.classList.remove('show');
    }
  });

  // Toggle the clicked dropdown
  const dropdownContent = event.target.nextElementSibling;
  if (dropdownContent) {
    dropdownContent.classList.toggle('show');
  }
}

function toggleLike(element) {
  const icon = element.querySelector('i');

  if (icon.classList.contains('far')) {

    icon.classList.remove('far');
    icon.classList.add('fas');
  } else {

    icon.classList.remove('fas');
    icon.classList.add('far');
  }


  element.classList.toggle('liked');


  icon.style.transform = "scale(1.2)";
  setTimeout(() => {
    icon.style.transform = "scale(1)";
  }, 300);
}


function goBack() {
  window.history.back();
}



// dropdowne js

function toggleDropdown(event) {
  // Close all other dropdowns first
  document.querySelectorAll('.dropdown-content').forEach((dropdown) => {
    if (dropdown !== event.target.nextElementSibling) {
      dropdown.classList.remove('show');
    }
  });

  // Toggle the clicked dropdown
  const dropdownContent = event.target.nextElementSibling;
  if (dropdownContent) {
    dropdownContent.classList.toggle('show');
  }
}


function toggleLike(element) {
  const icon = element.querySelector('i');

  if (icon.classList.contains('far')) {

    icon.classList.remove('far');
    icon.classList.add('fas');
  } else {

    icon.classList.remove('fas');
    icon.classList.add('far');
  }


  element.classList.toggle('liked');


  icon.style.transform = "scale(1.2)";
  setTimeout(() => {
    icon.style.transform = "scale(1)";
  }, 300);
}


function goBack() {
  window.history.back();
}



// dropdowne js

function toggleDropdown(event) {
  // Close all other dropdowns first
  document.querySelectorAll('.dropdown-content').forEach((dropdown) => {
    if (dropdown !== event.target.nextElementSibling) {
      dropdown.classList.remove('show');
    }
  });

  // Toggle the clicked dropdown
  const dropdownContent = event.target.nextElementSibling;
  if (dropdownContent) {
    dropdownContent.classList.toggle('show');
  }
}


// investor



document.addEventListener('DOMContentLoaded', () => {
  // Select all download buttons
  const downloadButtons = document.querySelectorAll('.download-btn');

  downloadButtons.forEach(button => {
    button.addEventListener('click', () => {
      const fileUrl = button.getAttribute('data-file');
      const fileName = button.getAttribute('data-name');

      // Create an invisible anchor element
      const link = document.createElement('a');
      link.href = fileUrl;
      link.download = fileName;

      // Trigger the download
      document.body.appendChild(link);
      link.click();

      // Clean up
      document.body.removeChild(link);
    });
  });
});






const navLinks = document.querySelectorAll('.nav-list li');
navLinks.forEach(link => {
  link.addEventListener('click', function () {
    navLinks.forEach(link => link.classList.remove('active'));
    this.classList.add('active');
  });
});


// sui dhaga

document.addEventListener("DOMContentLoaded", () => {
  const filterOptions = document.querySelectorAll(".filter-option");
  const sortDropdown = document.getElementById("sortDropdown");
  const productList = document.getElementById("product-list");

  const applyFiltersAndSort = () => {
    const selectedSort = sortDropdown.value;
    const activeFilters = {};

    filterOptions.forEach(option => {
      if (option.classList.contains("active")) {
        const filterType = option.getAttribute("data-filter");
        const filterValue = option.getAttribute("data-value");
        activeFilters[filterType] = filterValue;
      }
    });


    // Get all product cards as an array
    const productCards = Array.from(productList.querySelectorAll(".product-c"));

    // Filter products
    productCards.forEach(card => {
      let showCard = true;

      for (const filterType in activeFilters) {
        if (card.getAttribute(`data-${filterType}`) !== activeFilters[filterType]) {
          showCard = false;
          break;
        }
      }

      card.style.display = showCard ? "block" : "none";
    });



    // Sort products
    productCards
      .filter(card => card.style.display !== "none")
      .sort((a, b) => {
        if (selectedSort === "low-to-high") {
          return parseInt(a.querySelector(".product-info h5").textContent.replace(/₹|,/g, "")) - parseInt(b.querySelector(".product-info h5").textContent.replace(/₹|,/g, ""));
        } else if (selectedSort === "high-to-low") {
          return parseInt(b.querySelector(".product-info h5").textContent.replace(/₹|,/g, "")) - parseInt(a.querySelector(".product-info h5").textContent.replace(/₹|,/g, ""));
        } else {
          return 0;
        }
      })
      .forEach(card => productList.appendChild(card));
  };

  // Handle filter option clicks
  filterOptions.forEach(option => {
    option.addEventListener("click", (e) => {
      e.preventDefault();
      option.classList.toggle("active");
      applyFiltersAndSort();
    });
  });

  // Handle sort dropdown change
  sortDropdown.addEventListener("change", applyFiltersAndSort);
});


function toggleLike(element) {
  const icon = element.querySelector('i');

  if (icon.classList.contains('far')) {

    icon.classList.remove('far');
    icon.classList.add('fas');
  } else {

    icon.classList.remove('fas');
    icon.classList.add('far');
  }


  element.classList.toggle('liked');


  icon.style.transform = "scale(1.2)";
  setTimeout(() => {
    icon.style.transform = "scale(1)";
  }, 300);
}


function goBack() {
  window.history.back();
}



// dropdowne js

function toggleDropdown(event) {
  // Close all other dropdowns first
  document.querySelectorAll('.dropdown-content').forEach((dropdown) => {
    if (dropdown !== event.target.nextElementSibling) {
      dropdown.classList.remove('show');
    }
  });

  // Toggle the clicked dropdown
  const dropdownContent = event.target.nextElementSibling;
  if (dropdownContent) {
    dropdownContent.classList.toggle('show');
  }
}
function toggleLike(element) {
  const icon = element.querySelector('i');

  if (icon.classList.contains('far')) {

    icon.classList.remove('far');
    icon.classList.add('fas');
  } else {

    icon.classList.remove('fas');
    icon.classList.add('far');
  }


  element.classList.toggle('liked');


  icon.style.transform = "scale(1.2)";
  setTimeout(() => {
    icon.style.transform = "scale(1)";
  }, 300);
}


function goBack() {
  window.history.back();
}



// dropdowne js

function toggleDropdown(event) {
  // Close all other dropdowns first
  document.querySelectorAll('.dropdown-content').forEach((dropdown) => {
    if (dropdown !== event.target.nextElementSibling) {
      dropdown.classList.remove('show');
    }
  });

  // Toggle the clicked dropdown
  const dropdownContent = event.target.nextElementSibling;
  if (dropdownContent) {
    dropdownContent.classList.toggle('show');
  }
}

function toggleLike(element) {
  const icon = element.querySelector('i');

  if (icon.classList.contains('far')) {

    icon.classList.remove('far');
    icon.classList.add('fas');
  } else {

    icon.classList.remove('fas');
    icon.classList.add('far');
  }


  element.classList.toggle('liked');


  icon.style.transform = "scale(1.2)";
  setTimeout(() => {
    icon.style.transform = "scale(1)";
  }, 300);
}


function goBack() {
  window.history.back();
}



// dropdowne js

function toggleDropdown(event) {
  // Close all other dropdowns first
  document.querySelectorAll('.dropdown-content').forEach((dropdown) => {
    if (dropdown !== event.target.nextElementSibling) {
      dropdown.classList.remove('show');
    }
  });

  // Toggle the clicked dropdown
  const dropdownContent = event.target.nextElementSibling;
  if (dropdownContent) {
    dropdownContent.classList.toggle('show');
  }
}



function toggleLike(element) {
  const icon = element.querySelector('i');

  if (icon.classList.contains('far')) {

    icon.classList.remove('far');
    icon.classList.add('fas');
  } else {

    icon.classList.remove('fas');
    icon.classList.add('far');
  }


  element.classList.toggle('liked');


  icon.style.transform = "scale(1.2)";
  setTimeout(() => {
    icon.style.transform = "scale(1)";
  }, 300);
}




// dropdowne js

function toggleDropdown(event) {
  // Close all other dropdowns first
  document.querySelectorAll('.dropdown-content').forEach((dropdown) => {
    if (dropdown !== event.target.nextElementSibling) {
      dropdown.classList.remove('show');
    }
  });

  // Toggle the clicked dropdown
  const dropdownContent = event.target.nextElementSibling;
  if (dropdownContent) {
    dropdownContent.classList.toggle('show');
  }
}


function toggleLike(element) {
  const icon = element.querySelector('i');

  if (icon.classList.contains('far')) {

    icon.classList.remove('far');
    icon.classList.add('fas');
  } else {

    icon.classList.remove('fas');
    icon.classList.add('far');
  }


  element.classList.toggle('liked');


  icon.style.transform = "scale(1.2)";
  setTimeout(() => {
    icon.style.transform = "scale(1)";
  }, 300);
}


function goBack() {
  window.history.back();
}



// dropdowne js

function toggleDropdown(event) {
  // Close all other dropdowns first
  document.querySelectorAll('.dropdown-content').forEach((dropdown) => {
    if (dropdown !== event.target.nextElementSibling) {
      dropdown.classList.remove('show');
    }
  });

  // Toggle the clicked dropdown
  const dropdownContent = event.target.nextElementSibling;
  if (dropdownContent) {
    dropdownContent.classList.toggle('show');
  }
}