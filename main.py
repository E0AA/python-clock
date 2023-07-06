from datetime import datetime
import random, os, time, text

def move(y: int, x: int) -> None:
    print("\033[%d;%dH" % (y, x))

def get_time() -> str:
    return datetime.today().strftime("%I:%M:%S %p")

def get_date() -> str:
    return datetime.today().strftime("%m/%d/%Y")

def center(string: str) -> str:
    term_width: int = os.get_terminal_size().columns
    
    if "\n" in string:
        lines = string.split("\n")
        for index, line in enumerate(lines):
            padding: str = " " * ( (term_width - len(line)) // 2 )
            lines[index] = padding + line + padding
        
        return "\n".join(lines)
    else:
        padding: str = " " * ( (term_width - len(string)) // 2 )
    
        return padding + string + padding

def sync_with_seconds() -> None:
    now: str = get_time()
    while now == get_time():
        pass

def main() -> None:
    RUN = True
    
    ESC = "\x1B"
    
    colcode = lambda code, bold = False: f"{ESC}[{int(bold)};{code}m"
    
    runtime: int = 0
    color_switch_interval: int = 10
    
    # Black   - 30
    # Red     - 31
    # Green   - 32
    # Yellow  - 33
    # Blue    - 34
    # Magenta - 35
    # Cyan    - 36
    # White   - 37
    
    sync_with_seconds()
    
    while RUN:
        if runtime % color_switch_interval == 0:
            print(colcode(random.randint(31, 37)))
            
        move(0, 0)
        
        print(center("Made By E0AA"), end = "\n\n")
        
        text_date: str = text.generate_ascii(
            get_date()
        )
        text_time: str = text.generate_ascii(
            get_time()
        )
        
        print(center(text_date), end = "\n\n\n")
        
        for line in text_time.split("\n"):
            print(center(line))
            time.sleep(0.05)
        
        time.sleep(1 - (0.05 * len(text_time.split("\n"))))
        runtime += 1
    
if __name__ == "__main__":
    main()
