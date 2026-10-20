/*
 * Configuração do site Compramos Carros.
 *
 * formEndpoint: endereço que recebe os formulários (por exemplo um formulário
 *   Formspree: "https://formspree.io/f/xxxxxxx"). Enquanto estiver vazio, os pedidos
 *   são enviados por WhatsApp, já preenchidos com os dados do formulário.
 * aceitaFotos: true mostra o campo "Fotos do carro" no formulário de avaliação.
 *   Só funciona com um formEndpoint que receba ficheiros (por exemplo o CRM):
 *   as fotos seguem no campo "fotos", reduzidas para no máximo 1600 px.
 *   Enquanto estiver a false, o cliente é convidado a enviar as fotos por WhatsApp.
 */
window.CC_CONFIG = {
  formEndpoint: "https://leads.compramoscarros.pt/api/leads",
  aceitaFotos: false,
  whatsapp: "351912263717",
  telefone: "912 263 717",
  email: "comercial@compramos-carros.com"
};
