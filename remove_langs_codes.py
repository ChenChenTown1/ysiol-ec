import os
import sys

LANGUAGE_EXTENSIONS = [
    ".ab", ".aa", ".af", ".ak", ".sq", ".am", ".ar", ".hy", ".as", ".ay",
    ".az", ".bn", ".ba", ".eu", ".be", ".bho", ".bs", ".br", ".bg", ".my",
    ".ca", ".ceb", ".zh-Hans", ".zh-Hant", ".co", ".hr", ".cs", ".da", ".dv",
    ".nl", ".dz", ".en-orig", ".en", ".eo", ".et", ".ee", ".fo", ".fj", ".fil",
    ".fi", ".fr", ".gaa", ".gl", ".lg", ".ka", ".de", ".el", ".gn", ".gu",
    ".ht", ".ha", ".haw", ".iw", ".hi", ".hmn", ".hu", ".is", ".ig", ".id",
    ".iu", ".ga", ".it", ".ja", ".jv", ".kl", ".kn", ".kk", ".kha", ".km",
    ".rw", ".ko", ".kri", ".ku", ".ky", ".lo", ".la", ".lv", ".ln", ".lt",
    ".lua", ".luo", ".lb", ".mk", ".mg", ".ms", ".ml", ".mt", ".gv", ".mi",
    ".mr", ".mn", ".mfe", ".ne", ".new", ".nso", ".no", ".ny", ".oc", ".or",
    ".om", ".os", ".pam", ".ps", ".fa", ".pl", ".pt", ".pt-PT", ".pa", ".qu",
    ".ro", ".rn", ".ru", ".sm", ".sg", ".sa", ".gd", ".sr", ".crs", ".sn",
    ".sd", ".si", ".sk", ".sl", ".so", ".st", ".es", ".su", ".sw", ".ss",
    ".sv", ".tg", ".ta", ".tt", ".te", ".th", ".bo", ".ti", ".to", ".ts",
    ".tn", ".tum", ".tr", ".tk", ".uk", ".ur", ".ug", ".uz", ".ve", ".vi",
    ".war", ".cy", ".fy", ".wo", ".xh", ".yi", ".yo", ".zu"
]

def process_current_directory():
    current_dir = os.getcwd()
    
    if not os.path.isdir(current_dir):
        print(f"Error: Current directory '{current_dir}' is invalid")
        return
    
    sorted_extensions = sorted(LANGUAGE_EXTENSIONS, key=len, reverse=True)
    processed_files = 0
    renamed_files = 0
    
    for filename in os.listdir(current_dir):
        try:
            file_path = os.path.join(current_dir, filename)
            
            if not os.path.isfile(file_path):
                continue
            
            processed_files += 1
            current_name = filename
            
            for extension in sorted_extensions:
                if current_name.lower().endswith(extension.lower()):
                    actual_extension = current_name[-len(extension):]
                    new_name = current_name[:-len(actual_extension)]
                    new_file_path = os.path.join(current_dir, new_name)
                    
                    if os.path.exists(new_file_path):
                        print(f"Skip: '{current_name}' -> '{new_name}' (target exists)")
                        break
                    
                    try:
                        os.rename(file_path, new_file_path)
                        print(f"Done: '{current_name}' -> '{new_name}'")
                        renamed_files += 1
                        current_name = new_name
                        break
                    except Exception as error:
                        print(f"Error: Failed to rename '{current_name}': {error}")
                        break
        except Exception as error:
            print(f"Error processing file '{filename}': {error}")
    
    print(f"\nResult:")
    print(f"Total files: {processed_files}")
    print(f"Renamed files: {renamed_files}")

def main():
    print("Current directory:", os.getcwd())
    print("Will remove language extensions from all files")
    
    user_input = input("\nStart? (y/n): ").strip().lower()
    
    if user_input == 'y' or user_input == 'yes':
        print("\nProcessing...\n")
        process_current_directory()
    else:
        print("Cancelled")

if __name__ == "__main__":
    main()
