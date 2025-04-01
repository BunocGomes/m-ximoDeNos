from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(level_order: List[Optional[int]]) -> Optional[TreeNode]:
    """Constrói árvore binária a partir de lista nível por nível"""
    if not level_order or level_order[0] is None:
        return None
    
    root = TreeNode(level_order[0])
    queue = [root]
    idx = 1
    
    while queue and idx < len(level_order):
        current = queue.pop(0)
        
        # Processa filho esquerdo
        if idx < len(level_order) and level_order[idx] is not None:
            current.left = TreeNode(level_order[idx])
            queue.append(current.left)
        idx += 1
        
        # Processa filho direito
        if idx < len(level_order) and level_order[idx] is not None:
            current.right = TreeNode(level_order[idx])
            queue.append(current.right)
        idx += 1
    
    return root

def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """Travessia Pré-ordem (Raiz, Esquerda, Direita)"""
    result = []
    def traverse(node):
        if node:
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)
    traverse(root)
    return result

def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """Travessia Em-ordem (Esquerda, Raiz, Direita)"""
    result = []
    def traverse(node):
        if node:
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)
    traverse(root)
    return result

def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """Travessia Pós-ordem (Esquerda, Direita, Raiz)"""
    result = []
    def traverse(node):
        if node:
            traverse(node.left)
            traverse(node.right)
            result.append(node.val)
    traverse(root)
    return result

def calculate_depth(root: Optional[TreeNode]) -> int:
    """Calcula a profundidade máxima da árvore"""
    if not root:
        return 0
    return max(calculate_depth(root.left), calculate_depth(root.right)) + 1

def parse_input(input_str: str) -> List[Optional[int]]:
    """Converte string de entrada para lista de inteiros/None"""
    try:
        cleaned = input_str.strip()[1:-1]
        if not cleaned:
            return []
        
        elements = [elem.strip() for elem in cleaned.split(',')]
        return [int(elem) if elem.lower() not in ['none', 'null', ''] else None 
                for elem in elements]
    except Exception:
        raise ValueError("Formato inválido. Use: [2, 3, None, ...]")

def main():
    print("Análise de Árvore Binária - Profundidade e Travessias")
    
    while True:
        print("\nMenu:")
        print("1. Calcular profundidade e mostrar todas as travessias")
        print("2. Executar travessia específica")
        print("3. Sair")
        
        option = input("Escolha uma opção (1-3): ")
        
        if option == "3":
            print("Encerrando programa...")
            break
            
        if option not in ["1", "2"]:
            print("Opção inválida! Tente novamente.")
            continue
            
        print("\nDigite a árvore no formato [2,3,None,22,45,76,None,None]")
        input_str = input("Árvore: ")
        
        try:
            nodes = parse_input(input_str)
            root = build_tree(nodes)
            
            if not root:
                print("Árvore vazia!")
                continue
                
            if option == "1":
                depth = calculate_depth(root)
                print(f"\nProfundidade máxima: {depth}")
                
                print("\nTravessias:")
                print(f"Pré-ordem: {preorder_traversal(root)}")
                print(f"Em-ordem: {inorder_traversal(root)}")
                print(f"Pós-ordem: {postorder_traversal(root)}")
            
            else:
                print("\nTipos de travessia:")
                print("1. Pré-ordem (raiz, esquerda, direita)")
                print("2. Em-ordem (esquerda, raiz, direita)")
                print("3. Pós-ordem (esquerda, direita, raiz)")
                
                traversal_choice = input("Escolha a travessia (1-3): ")
                
                if traversal_choice == "1":
                    print("\nPré-ordem:", preorder_traversal(root))
                elif traversal_choice == "2":
                    print("\nEm-ordem:", inorder_traversal(root))
                elif traversal_choice == "3":
                    print("\nPós-ordem:", postorder_traversal(root))
                else:
                    print("Opção inválida!")
                
                depth = calculate_depth(root)
                print(f"\nProfundidade da árvore: {depth}")
                
        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
