from datetime import timedelta


def format_time(total_seconds):
    """
    Convert total seconds to SRT format 'hh:mm:ss,ms', ensuring leading zeros.
    """
    td = timedelta(seconds=total_seconds)
    total_seconds = int(total_seconds)
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = int((total_seconds - int(total_seconds)) * 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"


def convert_to_srt(input_file, output_file):
    """
    Convert text file to .srt format with proper formatting and numbering.
    """
    with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        lines = infile.readlines()
        srt_counter = 1
        last_end_time = 0
        current_start_time = 0  # Initialize to track the current start time
        subtitles = []
        current_text = ""  # Variable to accumulate text for the same timestamp

        # Read all subtitles into a list with start times and texts
        for line in lines:
            line = line.strip()
            if line:
                # Check if the line starts with a time stamp (e.g., "00:01:23")
                if ":" in line:
                    # If we have accumulated text, save the previous subtitle
                    if current_text:
                        subtitles.append((current_start_time, current_text.strip()))
                        current_text = ""  # Reset the current text

                    # Split the line only if it contains both time and text
                    parts = line.split(" ", 1)
                    if len(parts) > 1:  # Ensure there is both time and text
                        time_part, text = parts
                        start_time = sum(float(x) * 60 ** i for i, x in enumerate(reversed(time_part.split(":"))))
                        current_start_time = start_time  # Update the current start time
                        current_text = text.strip()  # Start accumulating text for this timestamp
                    else:
                        # Handle the case where only a time stamp is present
                        time_part = parts[0]
                        start_time = sum(float(x) * 60 ** i for i, x in enumerate(reversed(time_part.split(":"))))
                        current_start_time = start_time  # Update the current start time
                else:
                    # If the line doesn't have a timestamp, it belongs to the previous subtitle
                    current_text += " " + line.strip()

        # Append the last accumulated subtitle
        if current_text:
            subtitles.append((current_start_time, current_text.strip()))

        # Process subtitles and write to output file
        for i in range(len(subtitles)):
            start_time, text = subtitles[i]

            # Ensure at least 2 seconds of display time
            if i < len(subtitles) - 1:
                next_start_time = subtitles[i + 1][0]
                end_time = next_start_time - 0.01
            else:
                # If it's the last subtitle, set a default end time
                end_time = start_time + 2.0

            # Adjust start time if it overlaps with the previous subtitle
            if start_time < last_end_time:
                start_time = last_end_time + 0.001
                end_time = start_time + 2.0  # Adjust end time accordingly

            # Write subtitle entry
            outfile.write(f"{srt_counter}\n")
            outfile.write(f"{format_time(start_time)} --> {format_time(end_time)}\n")
            outfile.write(f"{text}\n\n")

            srt_counter += 1
            last_end_time = end_time


# File paths
input_file_path = "D:/movie/english/bob/1/make/NbqKRCefJhU.txt"  # Replace with your text file path
output_file_path = "D:/movie/english/bob/1/make/NbqKRCefJhU.srt"  # Replace with desired .srt file path

# Convert the file
convert_to_srt(input_file_path, output_file_path)

print(f"Converted {input_file_path} to {output_file_path}")
