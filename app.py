# DESAFIO_REVVO/app.py
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os

# Inicializar a aplicação Flask
app = Flask(__name__)
CORS(app)

# Dados iniciais
cursos = [
    {"id": 1, "titulo": "Desenvolvimento Web com Python", "descricao": "Aprenda a criar sites com Flask e Django."},
    {"id": 2, "titulo": "Banco de Dados SQL", "descricao": "Tudo sobre como modelar e gerenciar bases de dados."},
]

slides = [
    {"id": 1, "titulo": "LOREM IPSUM", "descricao": "Aenean lacinia bibendum nulla sed consectetur.", "imagem": "fundo-slideshow.png", "link": "#"},
    {"id": 2, "titulo": "SEGUNDO SLIDE", "descricao": "Conteúdo do segundo slide aqui...", "imagem": "fundo-slideshow-2.png", "link": "#"},
]

# Rota principal - servir o index.html
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

# Rotas para arquivos estáticos - IMPORTANTE!
@app.route('/assets/<path:path>')
def serve_assets(path):
    """Serve arquivos da pasta frontend/assets/"""
    return send_from_directory('frontend/assets', path)

@app.route('/favicon.ico')
def serve_favicon():
    return send_from_directory('.', 'favicon.ico')

# API Routes
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "API está funcionando"})

# ========== ROTAS PARA CURSOS ==========
@app.route('/api/cursos', methods=['GET'])
def get_cursos():
    return jsonify({"cursos": cursos})

@app.route('/api/cursos', methods=['POST'])
def create_curso():
    try:
        if not request.json or 'titulo' not in request.json or 'descricao' not in request.json:
            return jsonify({"error": "Título e descrição são obrigatórios"}), 400
        
        novo_curso = {
            "id": len(cursos) + 1,
            "titulo": request.json['titulo'],
            "descricao": request.json['descricao']
        }
        
        cursos.append(novo_curso)
        return jsonify(novo_curso), 201
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/cursos/<int:curso_id>', methods=['PUT'])
def update_curso(curso_id):
    try:
        curso = next((c for c in cursos if c['id'] == curso_id), None)
        if not curso:
            return jsonify({"error": "Curso não encontrado"}), 404
        
        if 'titulo' in request.json:
            curso['titulo'] = request.json['titulo']
        if 'descricao' in request.json:
            curso['descricao'] = request.json['descricao']
        
        return jsonify(curso)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/cursos/<int:curso_id>', methods=['DELETE'])
def delete_curso(curso_id):
    try:
        global cursos
        cursos = [c for c in cursos if c['id'] != curso_id]
        return jsonify({"message": "Curso deletado com sucesso"})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ========== ROTAS PARA SLIDES ==========
@app.route('/api/slides', methods=['GET'])
def get_slides():
    return jsonify({"slides": slides})

@app.route('/api/slides', methods=['POST'])
def create_slide():
    try:
        required_fields = ['titulo', 'descricao', 'imagem', 'link']
        if not request.json or any(field not in request.json for field in required_fields):
            return jsonify({"error": "Todos os campos são obrigatórios"}), 400
        
        novo_slide = {
            "id": len(slides) + 1,
            "titulo": request.json['titulo'],
            "descricao": request.json['descricao'],
            "imagem": request.json['imagem'],
            "link": request.json['link']
        }
        
        slides.append(novo_slide)
        return jsonify(novo_slide), 201
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ADICIONE ESTAS DUAS ROTAS QUE ESTAVAM FALTANDO:
@app.route('/api/slides/<int:slide_id>', methods=['PUT'])
def update_slide(slide_id):
    try:
        slide = next((s for s in slides if s['id'] == slide_id), None)
        if not slide:
            return jsonify({"error": "Slide não encontrado"}), 404
        
        # Atualizar apenas os campos fornecidos
        if 'titulo' in request.json:
            slide['titulo'] = request.json['titulo']
        if 'descricao' in request.json:
            slide['descricao'] = request.json['descricao']
        if 'imagem' in request.json:
            slide['imagem'] = request.json['imagem']
        if 'link' in request.json:
            slide['link'] = request.json['link']
        
        return jsonify(slide)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/slides/<int:slide_id>', methods=['DELETE'])
def delete_slide(slide_id):
    try:
        global slides
        slides = [s for s in slides if s['id'] != slide_id]
        return jsonify({"message": "Slide deletado com sucesso"})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Rota para a página de administração
@app.route('/admin')
def serve_admin():
    return send_from_directory('.', 'admin.html')

if __name__ == '__main__':
    print("=== SERVIDOR INICIADO ===")
    print("Estrutura de pastas:")
    print(f"- index.html existe: {os.path.exists('index.html')}")
    print(f"- frontend/assets existe: {os.path.exists('frontend/assets')}")
    print(f"- frontend/assets/css existe: {os.path.exists('frontend/assets/css')}")
    
    if os.path.exists('frontend/assets/css'):
        css_files = os.listdir('frontend/assets/css')
        print(f"- Arquivos CSS: {css_files}")
    
    print("\nURLs para testar:")
    print("1. http://localhost:5000/ - Página principal")
    print("2. http://localhost:5000/api/health - Saúde da API")
    print("3. http://localhost:5000/assets/css/main.css - Arquivo CSS")
    print("4. http://localhost:5000/assets/images/logo.png - Imagem")
    print("5. http://localhost:5000/admin - Painel administrativo")
    
    print("\nEndpoints da API:")
    print("GET    /api/cursos     - Listar cursos")
    print("POST   /api/cursos     - Criar curso")
    print("PUT    /api/cursos/:id - Atualizar curso")
    print("DELETE /api/cursos/:id - Excluir curso")
    print("GET    /api/slides     - Listar slides")
    print("POST   /api/slides     - Criar slide")
    print("PUT    /api/slides/:id - Atualizar slide")
    print("DELETE /api/slides/:id - Excluir slide")
    
    app.run(debug=True, host='0.0.0.0', port=5000)