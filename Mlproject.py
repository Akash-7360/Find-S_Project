# save as find_s_steps.py
import csv
import os

def load_csv(filename):
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return None, None
    with open(filename, 'r') as f:
        data = list(csv.reader(f))
        headers = data[0]
        examples = data[1:]
    return headers, examples

def pretty(h):
    # helper to show hypothesis as list or nice string
    return "[" + ", ".join(f"'{x}'" for x in h) + "]"

def find_s_step_by_step(examples):
    if not examples:
        return None

    # initialize most specific hypothesis
    hypothesis = ['0'] * (len(examples[0]) - 1)
    print("Initial hypothesis:", pretty(hypothesis))
    step = 0

    for idx, row in enumerate(examples, start=1):
        label = row[-1].strip().lower()
        attrs = row[:-1]
        print(f"\nExample {idx}: {attrs} -> Label: '{row[-1]}'")

        if label == "yes":
            step += 1
            # update hypothesis using this positive example
            for i in range(len(attrs)):
                val = attrs[i].strip()
                if hypothesis[i] == '0':
                    hypothesis[i] = val
                elif hypothesis[i] != val:
                    hypothesis[i] = '?'
            print(f"  Positive example -> updated hypothesis (step {step}): {pretty(hypothesis)}")
        else:
            print("  Negative example -> hypothesis unchanged")

    print("\nFinal hypothesis:", pretty(hypothesis))
    return hypothesis

def main():
    filename = input("Enter CSV path here: ").strip()
    headers, examples = load_csv(filename)
    if headers is None:
        return

    print("\nAttributes:", headers[:-1])
    find_s_step_by_step(examples)

if __name__ == "__main__":
    main()
