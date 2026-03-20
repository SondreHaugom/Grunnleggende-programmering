import os
file_path = os.path.join(os.path.dirname(__file__), "logg.txt")

def count_lines_in_file(file_path):
    # legger til startverdier for tellingen
    total_fails = 0
    total_ok = 0
    total_lines = 0
    user_line_counts = {}

    # åpner filen og leser innholdet, og håndterer eventuelle feil hvis filen ikke finnes
    try:
        with open(file_path, "r") as file:
            all_lines = file.readlines()
            # Henter ut alle linjer fra lista
            for line in all_lines:
                parts = line.strip().split(';')

                if line.strip():  # Check if the line is not empty
                    total_lines += 1
                

                # skjekker for antal FAIL og OK linher ved å sjekke siste kolonne i linjen
                if len(parts) >= 3 and parts[-1] == "FAIL":
                    total_fails += 1
                
                elif len(parts) >= 1 and parts[-1] == "OK":
                    total_ok += 1

                # teller linjer for hver bruker ved å sjekke andre kolonne i linjen
                if len(parts) >= 2:
                    name = parts[1]
                    if name in user_line_counts:
                        user_line_counts[name] += 1
                    else: 
                        user_line_counts[name] = 1


        # printer ut verdiene for total linjer, total FAIL linjer, total OK linjer og total linjer for hver bruker
        print(f"Total lines: {total_lines}")
        print(f"Total FAIL lines: {total_fails}")
        print(f"Total OK lines: {total_ok}")
        print("Total lines for each user:")
        for name, count in user_line_counts.items():
            print(f"{name}: {count}", "linjer")
 
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

# kaller funksjonen for å telle linjer i filen
count_lines_in_file(file_path)
