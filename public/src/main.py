from textnode import TextNode, TextType

def main():
    # Creating a dummy node to test the __repr__ and constructor
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

if __name__ == "__main__":
    main()