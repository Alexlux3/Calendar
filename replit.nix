{ pkgs }: {
  deps = [
    pkgs.python3
    pkgs.python3Packages.flask
    pkgs.python3Packages.schedule
    pkgs.python3Packages.requests
    # Añade otras dependencias necesarias aquí
  ];

  command = "tmux new-session -d -s mysession 'python main.py' && tmux split-window -v -t mysession 'python scheduler.py' && tmux -2 attach-session -t mysession";
}

