# Site Compramos Carros — compramoscarros.pt

Site estático (HTML, CSS e JavaScript, sem dependências), com a mesma estrutura, textos e
logotipo do site original.

| Página | Ficheiro |
|---|---|
| Início (formulário de avaliação) | `index.html` |
| Como funciona | `como-funciona.html` |
| Quem Somos | `quem-somos.html` |
| Centro de Entregas | `centro-de-entregas.html` |
| Contactos | `contactos.html` |
| Política de privacidade | `politica-de-privacidade.html` |
| Política de cookies | `politica-de-cookies.html` |

## Editar textos

As páginas são geradas por `ferramentas/gerar_site.py` (cabeçalho e rodapé num só sítio).
Altere esse ficheiro e corra:

```bash
python3 ferramentas/gerar_site.py
```

Para ver o site localmente: `python3 -m http.server --directory site 8000` e abrir
http://localhost:8000.

## Marcas e modelos

A lista do formulário de avaliação está em `site/assets/js/marcas.js` (73 marcas, incluindo
as que já só existem no mercado de usados). Para acrescentar uma marca ou um modelo basta
editar esse ficheiro; o formulário ordena tudo alfabeticamente. Quem não encontrar a sua
marca ou modelo escolhe "Outra marca" / "Outro modelo" e escreve-o num campo de texto.

## Versões (submodelos)

Nos modelos em que a versão muda muito o valor (BMW Série 1 → 116d, 118i…, Mercedes Classe C →
C 200, C 220 d…), o formulário mostra um passo "Versão" depois do modelo. As versões estão em
`site/assets/js/versoes.js` (BMW, Mercedes-Benz, Audi e Volvo; 72 modelos). Nos modelos que não
estão nessa lista o passo é saltado. "Outra / não sei" deixa sempre avançar. Os nomes da marca e do
modelo têm de ser iguais aos de `marcas.js`.

A seguir há o passo "Nível de equipamento" (Pack M, AMG Line, S line, Trendline, Sportline…),
por marca, em `CC_EQUIPAMENTOS` no mesmo ficheiro (14 marcas); nas outras marcas é saltado.

No CRM, o campo `versao` junta as duas escolhas ("118d · Pack M / M Sport"); seguem também em
separado em `versao_motor` e `nivel_equipamento`. "Outra / não sei" não entra em `versao`.

## Formulário de avaliação (passo a passo)

A página inicial usa um formulário em passos (`site/assets/js/assistente.js`):
marca → modelo → versão (só em alguns modelos) → nível de equipamento (só em algumas marcas) → ano e mês → caixa → segmento → matrícula, km e observações → fotos
(só com `aceitaFotos: true`) → dados de contacto. O envio é feito por `main.js`.

Campos enviados ao CRM: `marca`, `modelo`, `marca_outra`, `modelo_outro` (quando é
"Outra marca" / "Outro modelo"), `ano`, `mes`, `transmissao`, `segmento`, `matricula`,
`km`, `observacoes`, `nome`, `telefone`, `email`, `distrito`, `consentimento`, `_subject`
e, com fotos ativas, `fotos` (ficheiros).

## Formulários

Configurados em `assets/js/config.js`:

- Com `formEndpoint` vazio (por omissão), o pedido abre o WhatsApp para o 912 263 717 com
  todos os dados do formulário já preenchidos.
- Para receber os pedidos por email, crie um formulário gratuito em https://formspree.io
  (com o email da empresa) e coloque o endereço em `formEndpoint`,
  por exemplo `"https://formspree.io/f/abcd1234"`.


### Fotos do carro

Ligadas (`aceitaFotos: true` em `assets/js/config.js`): o passo "Fotos" do formulário de
avaliação aceita até 10 fotos, reduzidas no navegador para no máximo 1600 px (JPEG) e
enviadas ao CRM no campo `fotos` (`multipart/form-data`, ficheiros `foto-1.jpg`, …).

Se o envio com fotos falhar (erro do CRM ou da ligação), o pedido é reenviado
automaticamente sem fotos e com o campo `fotos_nao_enviadas` (número de fotos), e o
cliente é convidado a enviá-las por WhatsApp. Assim nenhuma lead se perde.
Para desligar as fotos basta voltar a pôr `aceitaFotos: false`.

## Publicação (Cloudflare)

O site é publicado pelo Cloudflare (Workers com ficheiros estáticos), ligado a este
repositório: cada alteração no ramo `main` é publicada automaticamente em 1 a 2 minutos.

- `wrangler.jsonc`: publica a pasta `site/` e usa `404.html` para endereços inexistentes.
- `site/_headers`: cabeçalhos de segurança (CSP, HSTS, X-Frame-Options, …), gerado por
  `ferramentas/gerar_site.py`.
- Os endereços das páginas não têm ".html" (`/como-funciona`); o Cloudflare serve-os a
  partir de `como-funciona.html` e reencaminha os endereços antigos com ".html".
- Domínios `compramoscarros.pt` e `www.compramoscarros.pt` ligados em
  Workers & Pages → compramoscarros-site → Domains.

## Pendentes

- [x] **Meta Pixel** (21/10/2026), ID 1312328063221205, em `site/assets/js/pixel.js`. Só arranca
  depois de o visitante carregar em "Aceitar" no aviso de cookies (que agora também tem "Recusar";
  a escolha fica em `localStorage` `cc_cookies_v2` e pode ser mudada em "Preferências de cookies",
  no rodapé). Eventos: **PageView** (todas as páginas), **Lead** (página Obrigado, uma vez por
  pedido), **Contact** (formulário de contactos) e **AvaliacaoPasso** (personalizado, a cada passo
  do formulário de avaliação, com o nome do passo). Política de cookies atualizada.
  Outros pixels (Google Ads/Analytics, TikTok…) seguem o mesmo modelo e precisam de ser
  acrescentados à política de segurança (`politica_seguranca()` no gerador).
- [x] **Mudança para o Cloudflare** (21/10/2026): domínios ligados ao Worker, GitHub Pages
  desligado, "Always Use HTTPS" ativo. HTTP Observatory: **A+ (135/100)** (antes D, 30/100).
- [x] Google Search Console (21/10/2026): propriedade de domínio compramoscarros.pt verificada,
  sitemap `https://compramoscarros.pt/sitemap.xml` enviado e indexação pedida.
- [x] www.compramoscarros.pt redireciona (301) para compramoscarros.pt, mantendo o caminho e
  os parâmetros (Cloudflare → compramoscarros.pt → Rules → Redirect Rules). O domínio www
  tem de continuar ligado ao Worker para o redirecionamento funcionar.
- [ ] (Opcional) Página de agradecimento própria para o formulário de Contactos, para medir
  também esses contactos.
- [ ] (CRM) Mostrar na lead o campo `fotos_nao_enviadas`, enviado quando as fotos falham e o
  pedido segue sem elas.
- [ ] (Opcional) Apagar o ramo antigo `claude/clever-cerf-2ke3aj` no repositório
  `Compramos-Carros`, que tem uma cópia antiga do site.
