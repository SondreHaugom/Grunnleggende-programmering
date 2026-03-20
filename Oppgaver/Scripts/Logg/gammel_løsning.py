# Gammel løsning.

file_path = "logg/Scripts/logg.txt"
try:
    with open(file_path, "r") as file:
        # Read all lines from the file
        all_lines = file.readlines()

        # Har et startpunkt for å telle linjer, fails, ok og linjer for hver bruker
        total_lines = 0
        total_fails = 0
        total_ok = 0
        total_lines_for_each_user = {}
        

        for line in all_lines:
            name_list.append(line.strip().split(';')[1])  # Assuming the name is always in the second column


        # Count non-empty lines
        for line in all_lines:
            if line:  # Check if the line is not empty
                total_lines += 1
            else:
                print(f"Empty line found: {line.strip()}")


        # Count lines that contain "FAIL"
        for line in all_lines:
            parts = line.strip().split(';')
            if len(parts) >= 3 and parts[-1] == "FAIL":  # Sjekker kun siste kolonne
                total_fails += 1


        for line in all_lines:
            parts = line.strip().split(';')



        for line in all_lines:
            parts = line.strip().split(';')
            if len(parts) >= 1 and parts[-1] == "OK":  # Sjekker kun siste kolonne
                total_ok += 1
            
        for line in all_lines:
            parts = line.strip().split(';')
            if len(parts) >= 2:
                name = name_list[all_lines.index(line)]  # Assuming the name is always in the second column¨
                if name in total_lines_for_each_user:
                    total_lines_for_each_user[name] += 1
                else:
                    total_lines_for_each_user[name] = 1
        
 

        # Print the results
        print(f"Total lines: {total_lines}")
        print(f"Total FAIL lines: {total_fails}")
        print(f"Total OK lines: {total_ok}")
        print("Total lines for each user:")
        for name, count in total_lines_for_each_user.items():
            print(f"{name}: {count}")

        
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")

