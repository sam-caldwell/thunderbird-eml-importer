import os
import sys
import mailbox
import argparse


def import_emails(input_dir: str, output_mailbox: str):
    """
    Import all .eml files from the specified input directory into a Thunderbird local mailbox.

    Args:
        input_dir (str): Path to the input directory containing .eml files.
        output_mailbox (str): Path to the Thunderbird local mailbox file.
    """
    # Ensure the input directory exists
    if not os.path.isdir(input_dir):
        print(f"Input directory '{input_dir}' does not exist.")
        sys.exit(1)

    # Create or open the mailbox
    mbox = mailbox.mbox(output_mailbox)

    # Iterate through all files in the input directory
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)

        # Process only .eml files
        if os.path.isfile(file_path) and filename.endswith(".eml"):
            with open(file_path, 'r', encoding='utf-8') as file:
                try:
                    # Add each email to the mailbox
                    msg = mailbox.mboxMessage(file)
                    mbox.add(msg)
                except Exception as e:
                    print(f"Failed to import {filename}: {e}")

    # Close the mailbox to save changes
    mbox.close()
    print(f"Imported emails into '{output_mailbox}'.")


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Import .eml files into a Thunderbird mailbox.")
    parser.add_argument('--in', dest='input_dir', required=True, help="Input directory containing .eml files.")
    parser.add_argument('--out', dest='output_mailbox', required=True, help="Output Thunderbird local mailbox file.")

    args = parser.parse_args()

    # Import emails
    import_emails(args.input_dir, args.output_mailbox)
