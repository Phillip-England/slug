import engine
from dotenv import load_dotenv

load_dotenv()
engine = engine.engine()

if __name__ == '__main__':
    print("Initalizing Slug...")
    engine.run()