const API = "http://127.0.0.1:5000/listar_usuarios";

const listarusuarios = async () => {
    const res = await fetch(API);
    const data = await res.json();
    console.log(data);
};

window.addEventListener("load",function() {
    listarusuarios();
});