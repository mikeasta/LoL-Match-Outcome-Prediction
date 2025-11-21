import subprocess

class PostgreSQLServer:
    def run(self):
        try:
            print("Starting local PostgreSQL server")
            subprocess.run("postgres", shell=True)
        except Exception as e:
            print(f"Server didnt start due to following error: {e}")

if __name__ == "__main__":
    server = PostgreSQLServer()
    server.run()