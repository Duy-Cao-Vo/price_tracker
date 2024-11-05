document.getElementById('product-form').addEventListener('submit', async function (e) {
    e.preventDefault();
    const url = document.getElementById('product-url').value;
    const response = await fetch(`http://localhost:8000/product?url=${encodeURIComponent(url)}`);
    const product = await response.json();
    displayProductInfo(product);
});

function displayProductInfo(product) {
    const productInfoDiv = document.getElementById('product-info');
    productInfoDiv.innerHTML = `
        <h2>${product.name}</h2>
        <p>Price: $${product.price}</p>
        <p>Rating: ${product.rating}</p>
        <p>Source: <a href="${product.source}" target="_blank">${product.source}</a></p>
    `;
    // Add logic to display relevant products and price chart
}