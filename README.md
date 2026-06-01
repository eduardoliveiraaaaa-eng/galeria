# 📷 Galeria PWA

Galeria de fotos e vídeos como Progressive Web App (PWA), com visual inspirado no iOS Photos.

## ✨ Funcionalidades

| Recurso | Status |
|---|---|
| Importar arquivos (seleção múltipla) | ✅ |
| Importar pasta inteira (File System Access API) | ✅ Chrome/Edge |
| Grade responsiva (2–5 colunas configurável) | ✅ |
| Visualização em tela cheia com swipe | ✅ |
| Zoom por pinça (até 5×) | ✅ |
| Duplo toque para zoom | ✅ |
| Reprodução de vídeos | ✅ |
| Favoritos persistentes (IndexedDB) | ✅ |
| Lixeira com expiração em 30 dias | ✅ |
| Busca por nome de arquivo | ✅ |
| Ordenação por data, nome, tamanho | ✅ |
| Informações do arquivo (dimensões, tamanho, data) | ✅ |
| Renomear arquivos | ✅ |
| Compartilhar via Web Share API | ✅ |
| Download de arquivos | ✅ |
| Tema escuro / claro | ✅ |
| Álbuns automáticos (Câmera, Fotos, Vídeos, Favoritos) | ✅ |
| Álbuns criados pelo usuário | ✅ |
| Drag & drop para importar | ✅ |
| Modo de seleção múltipla | ✅ |
| Offline (Service Worker) | ✅ |
| Instalável como app (PWA) | ✅ |
| Navegação por teclado (←/→/Esc) | ✅ |
| Cache de miniaturas (IndexedDB) | ✅ |
| Suporte a orientação retrato e paisagem | ✅ |
| safe-area-inset para notch/barra home | ✅ |

## 🚀 Como usar

### Opção 1 — Abrir direto no navegador
Basta abrir o `index.html` em qualquer navegador moderno.

### Opção 2 — Servidor local (recomendado para PWA completo)
```bash
# Python
python3 -m http.server 8080

# Node
npx serve .

# PHP
php -S localhost:8080
```
Acesse: `http://localhost:8080`

### Opção 3 — Deploy gratuito
- **Netlify**: arraste a pasta para netlify.com/drop
- **Vercel**: `vercel deploy`
- **GitHub Pages**: coloque os arquivos no repositório

## 📱 Instalar como app

1. Abra no Chrome (Android) ou Safari (iOS)
2. **Android**: Menu → "Adicionar à tela inicial" ou banner automático
3. **iOS**: Compartilhar → "Adicionar à tela de início"
4. **Desktop**: ícone de instalação na barra de endereços

## 📁 Estrutura

```
galeria-pwa/
├── index.html        # App completo (HTML + CSS + JS)
├── manifest.json     # Manifesto PWA
├── sw.js             # Service Worker (offline)
├── icons/            # Ícones para instalação
│   ├── icon-72.png
│   ├── icon-96.png
│   ├── icon-128.png
│   ├── icon-192.png
│   └── icon-512.png
└── README.md
```

## 🔒 Privacidade

- **100% local** — nenhuma foto sai do dispositivo
- Armazenamento via IndexedDB (no próprio navegador)
- Sem servidor, sem upload, sem analytics

## 🌐 Compatibilidade

| Navegador | Importar pasta | Web Share | Instalar |
|---|---|---|---|
| Chrome Android | ✅ | ✅ | ✅ |
| Chrome Desktop | ✅ | ✅ | ✅ |
| Safari iOS | ⚠️ arquivos | ✅ | ✅ |
| Firefox | ⚠️ arquivos | ❌ | ❌ |
| Edge | ✅ | ✅ | ✅ |

## ⚠️ Limitações vs app nativo

- Sem acesso direto ao rolo da câmera (MediaStore)
- Fotos precisam ser importadas manualmente
- Espaço limitado pelo storage do navegador (~quota do dispositivo)
- Sem edição de EXIF (somente leitura de metadados básicos)
