# Python Automation Guide: Automate Your Daily Tasks

## Table of Contents

1. [Introduction to Automation](#introduction-to-automation)
2. [Why Automate with Python?](#why-automate-with-python)
3. [Essential Libraries for Automation](#essential-libraries-for-automation)
4. [Main Project: File Organization Automation](#main-project-file-organization-automation)
   - [Problem: Messy Downloads Folder](#problem-messy-downloads-folder)
   - [Solution Overview](#solution-overview)
   - [Step-by-Step Implementation](#step-by-step-implementation)
   - [Enhanced Version with Features](#enhanced-version-with-features)
5. [Additional Automation Examples](#additional-automation-examples)
   - [Email Automation](#email-automation)
   - [Web Data Collection](#web-data-collection)
   - [Excel/CSV Processing](#excelcsv-processing)
   - [System Backup Automation](#system-backup-automation)
   - [Report Generation](#report-generation)
6. [Scheduling Your Automation](#scheduling-your-automation)
7. [Error Handling and Logging](#error-handling-and-logging)
8. [Best Practices for Automation](#best-practices-for-automation)
9. [Testing Your Automation](#testing-your-automation)
10. [Expanding Your Automation Skills](#expanding-your-automation-skills)

---

## Introduction to Automation

**Automation** means making a computer do repetitive tasks for you automatically. Instead of manually organizing files, sending emails, or processing data every day, you write a Python script once and let it handle these tasks forever.

**Examples of tasks you can automate:**
- Organizing downloaded files into folders
- Sending daily reports via email
- Backing up important files
- Collecting data from websites
- Processing spreadsheets
- Renaming hundreds of files
- Monitoring system performance
- Creating daily/weekly reports

## Why Automate with Python?

**1. Save Time**: What takes hours manually can be done in seconds
**2. Reduce Errors**: Computers don't make typos or forget steps
**3. Consistency**: Same process every time, exactly as programmed
**4. Free Up Mental Energy**: Focus on important work, not repetitive tasks
**5. Work While You Sleep**: Automation runs 24/7

**Real-world impact:**
```
Manual file organization: 30 minutes daily = 182 hours yearly
Python automation: 2 seconds daily = 12 minutes yearly
Time saved: 181 hours and 48 minutes per year!
```

## Essential Libraries for Automation

Before we start, let's understand the key Python libraries for automation:

```python
# Built-in libraries (come with Python)
import os        # File and directory operations
import shutil    # File copying and moving
import datetime  # Date and time handling
import pathlib   # Modern path handling
import glob      # File pattern matching
import time      # Delays and timing
import logging   # Recording what your script does

# External libraries (install with: pip install library_name)
import schedule  # Job scheduling
import requests  # Web requests and API calls
import pandas    # Data processing
import openpyxl  # Excel file handling
import smtplib   # Email sending

# Installation commands for external libraries:
# pip install schedule requests pandas openpyxl
```

## Main Project: File Organization Automation

### Problem: Messy Downloads Folder

Most people have a Downloads folder that looks like this:
```
Downloads/
├── document.pdf
├── photo.jpg
├── report.xlsx
├── song.mp3
├── presentation.pptx
├── another_photo.png
├── spreadsheet.csv
├── video.mp4
└── ... (hundreds more files)
```

**Manual solution**: Spend 30 minutes every week sorting files into folders
**Automated solution**: Python script that organizes files instantly

### Solution Overview

Our automation will:
1. **Scan** the Downloads folder for files
2. **Identify** file types by their extensions
3. **Create** organized folders if they don't exist
4. **Move** files to appropriate folders
5. **Log** what was moved for review
6. **Handle** errors gracefully

### Step-by-Step Implementation

#### Step 1: Basic File Organizer

```python
import os
import shutil
from pathlib import Path

def organize_downloads():
    """
    Organize files in Downloads folder by type.
    """
    # Get the Downloads folder path
    downloads_path = Path.home() / "Downloads"
    
    # Define file categories and their extensions
    file_categories = {
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv"],
        "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
        "Spreadsheets": [".xlsx", ".xls", ".csv"],
        "Presentations": [".pptx", ".ppt"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Programs": [".exe", ".msi", ".dmg", ".pkg"]
    }
    
    print(f"Organizing files in: {downloads_path}")
    
    # Process each file in Downloads
    for file_path in downloads_path.iterdir():
        # Skip if it's a directory
        if file_path.is_dir():
            continue
            
        # Get file extension
        file_extension = file_path.suffix.lower()
        
        # Find which category this file belongs to
        moved = False
        for category, extensions in file_categories.items():
            if file_extension in extensions:
                # Create category folder if it doesn't exist
                category_folder = downloads_path / category
                category_folder.mkdir(exist_ok=True)
                
                # Move the file
                destination = category_folder / file_path.name
                shutil.move(str(file_path), str(destination))
                print(f"Moved: {file_path.name} → {category}/")
                moved = True
                break
        
        # If file type not recognized, put in "Other" folder
        if not moved:
            other_folder = downloads_path / "Other"
            other_folder.mkdir(exist_ok=True)
            destination = other_folder / file_path.name
            shutil.move(str(file_path), str(destination))
            print(f"Moved: {file_path.name} → Other/")
    
    print("Organization complete!")

# Run the organizer
if __name__ == "__main__":
    organize_downloads()
```

#### Step 2: Enhanced Version with Error Handling

```python
import os
import shutil
import logging
from pathlib import Path
from datetime import datetime

def setup_logging():
    """Set up logging to track what the script does."""
    log_filename = f"file_organizer_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler()  # Also print to console
        ]
    )
    return log_filename

def organize_downloads_enhanced():
    """
    Enhanced file organizer with error handling and logging.
    """
    log_file = setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        # Get the Downloads folder path
        downloads_path = Path.home() / "Downloads"
        
        if not downloads_path.exists():
            logger.error(f"Downloads folder not found: {downloads_path}")
            return
        
        # Define file categories
        file_categories = {
            "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"],
            "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".tiff"],
            "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"],
            "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
            "Spreadsheets": [".xlsx", ".xls", ".csv", ".ods"],
            "Presentations": [".pptx", ".ppt", ".odp"],
            "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
            "Programs": [".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm"],
            "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c"]
        }
        
        logger.info(f"Starting organization of: {downloads_path}")
        files_moved = 0
        errors = 0
        
        # Process each file
        for file_path in downloads_path.iterdir():
            try:
                # Skip directories and hidden files
                if file_path.is_dir() or file_path.name.startswith('.'):
                    continue
                
                file_extension = file_path.suffix.lower()
                moved = False
                
                # Find appropriate category
                for category, extensions in file_categories.items():
                    if file_extension in extensions:
                        # Create category folder
                        category_folder = downloads_path / category
                        category_folder.mkdir(exist_ok=True)
                        
                        # Handle duplicate names
                        destination = category_folder / file_path.name
                        counter = 1
                        while destination.exists():
                            name_parts = file_path.stem, counter, file_path.suffix
                            new_name = f"{name_parts[0]}_{name_parts[1]}{name_parts[2]}"
                            destination = category_folder / new_name
                            counter += 1
                        
                        # Move the file
                        shutil.move(str(file_path), str(destination))
                        logger.info(f"Moved: {file_path.name} → {category}/{destination.name}")
                        files_moved += 1
                        moved = True
                        break
                
                # Handle unrecognized file types
                if not moved:
                    other_folder = downloads_path / "Other"
                    other_folder.mkdir(exist_ok=True)
                    
                    destination = other_folder / file_path.name
                    counter = 1
                    while destination.exists():
                        name_parts = file_path.stem, counter, file_path.suffix
                        new_name = f"{name_parts[0]}_{name_parts[1]}{name_parts[2]}"
                        destination = other_folder / new_name
                        counter += 1
                    
                    shutil.move(str(file_path), str(destination))
                    logger.info(f"Moved: {file_path.name} → Other/{destination.name}")
                    files_moved += 1
                    
            except Exception as e:
                logger.error(f"Error processing {file_path.name}: {str(e)}")
                errors += 1
        
        # Summary
        logger.info(f"Organization complete! Files moved: {files_moved}, Errors: {errors}")
        logger.info(f"Log saved to: {log_file}")
        
    except Exception as e:
        logger.error(f"Critical error: {str(e)}")

# Run the enhanced organizer
if __name__ == "__main__":
    organize_downloads_enhanced()
```

#### Step 3: Configurable Version

```python
import os
import shutil
import logging
import json
from pathlib import Path
from datetime import datetime

class FileOrganizer:
    """
    Configurable file organizer that can be customized for different needs.
    """
    
    def __init__(self, config_file="organizer_config.json"):
        """Initialize with configuration file."""
        self.config_file = config_file
        self.load_config()
        self.setup_logging()
    
    def load_config(self):
        """Load configuration from JSON file or create default."""
        default_config = {
            "source_folder": str(Path.home() / "Downloads"),
            "categories": {
                "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"],
                "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".tiff"],
                "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"],
                "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
                "Spreadsheets": [".xlsx", ".xls", ".csv", ".ods"],
                "Presentations": [".pptx", ".ppt", ".odp"],
                "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
                "Programs": [".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm"],
                "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c"]
            },
            "create_date_folders": False,
            "handle_duplicates": True,
            "dry_run": False
        }
        
        if Path(self.config_file).exists():
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = default_config
            self.save_config()
    
    def save_config(self):
        """Save current configuration to file."""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)
    
    def setup_logging(self):
        """Set up logging."""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_filename = f"file_organizer_{timestamp}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_filename),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        self.log_file = log_filename
    
    def organize_files(self):
        """Main organization method."""
        source_path = Path(self.config["source_folder"])
        
        if not source_path.exists():
            self.logger.error(f"Source folder not found: {source_path}")
            return
        
        self.logger.info(f"Starting organization of: {source_path}")
        
        if self.config["dry_run"]:
            self.logger.info("DRY RUN MODE - No files will be moved")
        
        files_processed = 0
        files_moved = 0
        errors = 0
        
        for file_path in source_path.iterdir():
            try:
                if file_path.is_dir() or file_path.name.startswith('.'):
                    continue
                
                files_processed += 1
                destination = self.get_destination(file_path)
                
                if destination:
                    if not self.config["dry_run"]:
                        # Create destination directory
                        destination.parent.mkdir(parents=True, exist_ok=True)
                        shutil.move(str(file_path), str(destination))
                    
                    self.logger.info(f"{'Would move' if self.config['dry_run'] else 'Moved'}: "
                                   f"{file_path.name} → {destination.relative_to(source_path)}")
                    files_moved += 1
                
            except Exception as e:
                self.logger.error(f"Error processing {file_path.name}: {str(e)}")
                errors += 1
        
        self.logger.info(f"Processing complete! "
                        f"Files processed: {files_processed}, "
                        f"Files moved: {files_moved}, "
                        f"Errors: {errors}")
    
    def get_destination(self, file_path):
        """Determine where a file should be moved."""
        source_path = Path(self.config["source_folder"])
        file_extension = file_path.suffix.lower()
        
        # Find category
        category = "Other"
        for cat, extensions in self.config["categories"].items():
            if file_extension in extensions:
                category = cat
                break
        
        # Build destination path
        if self.config["create_date_folders"]:
            # Get file modification date
            mod_time = datetime.fromtimestamp(file_path.stat().st_mtime)
            date_folder = mod_time.strftime("%Y-%m")
            destination_dir = source_path / category / date_folder
        else:
            destination_dir = source_path / category
        
        destination = destination_dir / file_path.name
        
        # Handle duplicates
        if self.config["handle_duplicates"] and destination.exists():
            counter = 1
            while destination.exists():
                name_parts = file_path.stem, counter, file_path.suffix
                new_name = f"{name_parts[0]}_{name_parts[1]}{name_parts[2]}"
                destination = destination_dir / new_name
                counter += 1
        
        return destination
    
    def run_interactive_setup(self):
        """Interactive setup for configuration."""
        print("=== File Organizer Setup ===")
        
        # Source folder
        current_source = self.config["source_folder"]
        new_source = input(f"Source folder [{current_source}]: ").strip()
        if new_source:
            self.config["source_folder"] = new_source
        
        # Dry run option
        dry_run = input("Run in dry-run mode? (y/N): ").lower().startswith('y')
        self.config["dry_run"] = dry_run
        
        # Date folders
        date_folders = input("Create date-based subfolders? (y/N): ").lower().startswith('y')
        self.config["create_date_folders"] = date_folders
        
        self.save_config()
        print("Configuration saved!")
        
        # Run organization
        if input("Run organization now? (Y/n): ").lower() != 'n':
            self.organize_files()

# Usage examples
if __name__ == "__main__":
    # Option 1: Run with defaults
    organizer = FileOrganizer()
    organizer.organize_files()
    
    # Option 2: Interactive setup
    # organizer = FileOrganizer()
    # organizer.run_interactive_setup()
    
    # Option 3: Customize configuration
    # organizer = FileOrganizer()
    # organizer.config["dry_run"] = True  # Test mode
    # organizer.config["create_date_folders"] = True
    # organizer.organize_files()
```

### Enhanced Version with Features

```python
# Save this as file_organizer_pro.py
import os
import shutil
import logging
import schedule
import time
import tkinter as tk
from tkinter import messagebox, filedialog
from pathlib import Path
from datetime import datetime
import threading

class FileOrganizerGUI:
    """
    GUI version of the file organizer with scheduling capabilities.
    """
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File Organizer Pro")
        self.root.geometry("500x400")
        
        self.source_folder = tk.StringVar(value=str(Path.home() / "Downloads"))
        self.auto_organize = tk.BooleanVar()
        self.create_date_folders = tk.BooleanVar()
        
        self.setup_gui()
        self.setup_logging()
    
    def setup_gui(self):
        """Create the GUI interface."""
        # Title
        title_label = tk.Label(self.root, text="File Organizer Pro", 
                              font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Source folder selection
        folder_frame = tk.Frame(self.root)
        folder_frame.pack(pady=10, padx=20, fill="x")
        
        tk.Label(folder_frame, text="Source Folder:").pack(anchor="w")
        
        folder_entry_frame = tk.Frame(folder_frame)
        folder_entry_frame.pack(fill="x")
        
        folder_entry = tk.Entry(folder_entry_frame, textvariable=self.source_folder)
        folder_entry.pack(side="left", fill="x", expand=True)
        
        browse_btn = tk.Button(folder_entry_frame, text="Browse", 
                              command=self.browse_folder)
        browse_btn.pack(side="right", padx=(5, 0))
        
        # Options
        options_frame = tk.Frame(self.root)
        options_frame.pack(pady=10, padx=20, fill="x")
        
        tk.Checkbutton(options_frame, text="Create date-based subfolders",
                      variable=self.create_date_folders).pack(anchor="w")
        
        tk.Checkbutton(options_frame, text="Auto-organize every hour",
                      variable=self.auto_organize).pack(anchor="w")
        
        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        
        organize_btn = tk.Button(button_frame, text="Organize Now", 
                                command=self.organize_now, bg="green", fg="white")
        organize_btn.pack(side="left", padx=5)
        
        schedule_btn = tk.Button(button_frame, text="Start Auto-Organize", 
                                command=self.toggle_auto_organize)
        schedule_btn.pack(side="left", padx=5)
        
        # Status area
        self.status_text = tk.Text(self.root, height=15, width=60)
        self.status_text.pack(pady=10, padx=20, fill="both", expand=True)
        
        scrollbar = tk.Scrollbar(self.status_text)
        scrollbar.pack(side="right", fill="y")
        self.status_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.status_text.yview)
    
    def setup_logging(self):
        """Set up logging to display in GUI."""
        # Create custom handler for GUI
        self.gui_handler = GUILogHandler(self.status_text)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(message)s',
            handlers=[
                self.gui_handler,
                logging.FileHandler('file_organizer_gui.log')
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def browse_folder(self):
        """Open folder selection dialog."""
        folder = filedialog.askdirectory(initialdir=self.source_folder.get())
        if folder:
            self.source_folder.set(folder)
    
    def organize_now(self):
        """Run organization immediately."""
        threading.Thread(target=self._organize_files, daemon=True).start()
    
    def toggle_auto_organize(self):
        """Toggle automatic organization."""
        if self.auto_organize.get():
            schedule.every().hour.do(self._organize_files)
            self.logger.info("Auto-organization enabled (every hour)")
            threading.Thread(target=self._run_scheduler, daemon=True).start()
        else:
            schedule.clear()
            self.logger.info("Auto-organization disabled")
    
    def _run_scheduler(self):
        """Run the scheduler in background."""
        while self.auto_organize.get():
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    
    def _organize_files(self):
        """The actual file organization logic."""
        try:
            source_path = Path(self.source_folder.get())
            
            if not source_path.exists():
                self.logger.error(f"Source folder not found: {source_path}")
                return
            
            # File categories
            categories = {
                "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf"],
                "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
                "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
                "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
                "Spreadsheets": [".xlsx", ".xls", ".csv"],
                "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
                "Other": []
            }
            
            self.logger.info(f"Starting organization of: {source_path}")
            files_moved = 0
            
            for file_path in source_path.iterdir():
                if file_path.is_dir() or file_path.name.startswith('.'):
                    continue
                
                file_extension = file_path.suffix.lower()
                moved = False
                
                for category, extensions in categories.items():
                    if category == "Other":
                        continue
                    
                    if file_extension in extensions:
                        # Create destination
                        if self.create_date_folders.get():
                            mod_time = datetime.fromtimestamp(file_path.stat().st_mtime)
                            date_folder = mod_time.strftime("%Y-%m")
                            dest_dir = source_path / category / date_folder
                        else:
                            dest_dir = source_path / category
                        
                        dest_dir.mkdir(parents=True, exist_ok=True)
                        
                        # Move file
                        destination = dest_dir / file_path.name
                        counter = 1
                        while destination.exists():
                            name = f"{file_path.stem}_{counter}{file_path.suffix}"
                            destination = dest_dir / name
                            counter += 1
                        
                        shutil.move(str(file_path), str(destination))
                        self.logger.info(f"Moved: {file_path.name} → {category}/")
                        files_moved += 1
                        moved = True
                        break
                
                # Handle unrecognized files
                if not moved:
                    other_dir = source_path / "Other"
                    other_dir.mkdir(exist_ok=True)
                    destination = other_dir / file_path.name
                    counter = 1
                    while destination.exists():
                        name = f"{file_path.stem}_{counter}{file_path.suffix}"
                        destination = other_dir / name
                        counter += 1
                    
                    shutil.move(str(file_path), str(destination))
                    self.logger.info(f"Moved: {file_path.name} → Other/")
                    files_moved += 1
            
            self.logger.info(f"Organization complete! Files moved: {files_moved}")
            
        except Exception as e:
            self.logger.error(f"Error during organization: {str(e)}")
    
    def run(self):
        """Start the GUI application."""
        self.root.mainloop()

class GUILogHandler(logging.Handler):
    """Custom logging handler for GUI text widget."""
    
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget
    
    def emit(self, record):
        msg = self.format(record)
        self.text_widget.insert(tk.END, msg + "\n")
        self.text_widget.see(tk.END)  # Auto-scroll to bottom

# Run the GUI application
if __name__ == "__main__":
    app = FileOrganizerGUI()
    app.run()
```

## Additional Automation Examples

### Email Automation

```python
import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def send_daily_report():
    """Send a daily report email automatically."""
    
    # Email configuration (use environment variables for security)
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    EMAIL = "your_email@gmail.com"
    PASSWORD = "your_app_password"  # Use app password, not regular password
    
    # Create report content
    report_content = f"""
    Daily Report - {datetime.now().strftime('%Y-%m-%d')}
    
    System Status: ✅ Running
    Files Organized: {count_organized_files()}
    Disk Space: {get_disk_space()}
    
    Generated automatically by Python automation.
    """
    
    try:
        # Create email
        msg = MIMEMultipart()
        msg['From'] = EMAIL
        msg['To'] = "recipient@email.com"
        msg['Subject'] = f"Daily Report - {datetime.now().strftime('%Y-%m-%d')}"
        
        msg.attach(MIMEText(report_content, 'plain'))
        
        # Send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL, "recipient@email.com", text)
        server.quit()
        
        print("Daily report sent successfully!")
        
    except Exception as e:
        print(f"Error sending email: {e}")

def count_organized_files():
    """Count files in organized folders."""
    # Implementation depends on your folder structure
    return 42

def get_disk_space():
    """Get disk space information."""
    import shutil
    total, used, free = shutil.disk_usage("/")
    return f"{free // (2**30)} GB free"

# Schedule the email
schedule.every().day.at("09:00").do(send_daily_report)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)
```

### Web Data Collection

```python
import requests
import csv
import schedule
import time
from datetime import datetime

def collect_weather_data():
    """Collect weather data and save to CSV."""
    
    # Free weather API (get your key from openweathermap.org)
    API_KEY = "your_api_key"
    CITY = "London"
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(URL)
        data = response.json()
        
        # Extract relevant information
        weather_info = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"]
        }
        
        # Save to CSV
        filename = "weather_data.csv"
        file_exists = Path(filename).exists()
        
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=weather_info.keys())
            
            # Write header if file is new
            if not file_exists:
                writer.writeheader()
            
            writer.writerow(weather_info)
        
        print(f"Weather data collected: {weather_info['temperature']}°C, {weather_info['description']}")
        
    except Exception as e:
        print(f"Error collecting weather data: {e}")

# Collect weather data every hour
schedule.every().hour.do(collect_weather_data)

# Or collect stock prices
def collect_stock_prices():
    """Collect stock prices from a free API."""
    
    # Example using Alpha Vantage (free tier available)
    API_KEY = "your_api_key"
    SYMBOL = "AAPL"
    URL = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={SYMBOL}&apikey={API_KEY}"
    
    try:
        response = requests.get(URL)
        data = response.json()
        
        quote = data["Global Quote"]
        stock_info = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "symbol": quote["01. symbol"],
            "price": quote["05. price"],
            "change": quote["09. change"],
            "change_percent": quote["10. change percent"]
        }
        
        # Save to CSV
        with open("stock_data.csv", 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=stock_info.keys())
            writer.writerow(stock_info)
        
        print(f"Stock data collected: {stock_info['symbol']} - ${stock_info['price']}")
        
    except Exception as e:
        print(f"Error collecting stock data: {e}")
```

### Excel/CSV Processing

```python
import pandas as pd
import schedule
from pathlib import Path
from datetime import datetime

def process_sales_data():
    """Automatically process daily sales data."""
    
    input_folder = Path("input_data")
    output_folder = Path("processed_data")
    output_folder.mkdir(exist_ok=True)
    
    # Find today's sales file
    today = datetime.now().strftime("%Y-%m-%d")
    sales_file = input_folder / f"sales_{today}.csv"
    
    if not sales_file.exists():
        print(f"No sales file found for {today}")
        return
    
    try:
        # Read the data
        df = pd.read_csv(sales_file)
        
        # Process the data
        df['date'] = pd.to_datetime(df['date'])
        df['total'] = df['quantity'] * df['price']
        
        # Create summary statistics
        summary = {
            'total_sales': df['total'].sum(),
            'average_order': df['total'].mean(),
            'total_orders': len(df),
            'top_product': df.groupby('product')['total'].sum().idxmax()
        }
        
        # Save processed data
        output_file = output_folder / f"processed_sales_{today}.csv"
        df.to_csv(output_file, index=False)
        
        # Save summary
        summary_file = output_folder / f"summary_{today}.csv"
        summary_df = pd.DataFrame([summary])
        summary_df.to_csv(summary_file, index=False)
        
        print(f"Processed sales data: ${summary['total_sales']:.2f} total sales")
        
        # Send alert if sales are low
        if summary['total_sales'] < 1000:
            send_alert_email(f"Low sales alert: Only ${summary['total_sales']:.2f} today")
        
    except Exception as e:
        print(f"Error processing sales data: {e}")

def send_alert_email(message):
    """Send alert email (simplified version)."""
    print(f"ALERT: {message}")
    # Implement actual email sending here

# Run every day at 6 PM
schedule.every().day.at("18:00").do(process_sales_data)
```

### System Backup Automation

```python
import shutil
import schedule
import logging
from pathlib import Path
from datetime import datetime

def create_backup():
    """Create automated backup of important folders."""
    
    # Configure what to backup
    backup_sources = [
        Path.home() / "Documents",
        Path.home() / "Desktop",
        Path.home() / "Pictures"
    ]
    
    # Where to save backups
    backup_destination = Path.home() / "Backups"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    try:
        backup_destination.mkdir(exist_ok=True)
        
        for source in backup_sources:
            if source.exists():
                # Create backup folder name
                backup_name = f"{source.name}_{timestamp}"
                destination = backup_destination / backup_name
                
                # Copy the entire directory
                shutil.copytree(source, destination)
                print(f"Backed up: {source} → {destination}")
        
        # Clean up old backups (keep only last 7 days)
        cleanup_old_backups(backup_destination, days_to_keep=7)
        
        print(f"Backup completed successfully at {datetime.now()}")
        
    except Exception as e:
        print(f"Backup failed: {e}")

def cleanup_old_backups(backup_folder, days_to_keep=7):
    """Remove backups older than specified days."""
    
    cutoff_time = datetime.now().timestamp() - (days_to_keep * 24 * 60 * 60)
    
    for backup_dir in backup_folder.iterdir():
        if backup_dir.is_dir():
            if backup_dir.stat().st_mtime < cutoff_time:
                shutil.rmtree(backup_dir)
                print(f"Removed old backup: {backup_dir}")

# Schedule weekly backups
schedule.every().sunday.at("02:00").do(create_backup)

# Or run immediately for testing
if __name__ == "__main__":
    create_backup()
```

### Report Generation

```python
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime, timedelta
import schedule

def generate_monthly_report():
    """Generate comprehensive monthly report with charts."""
    
    # Get last month's data
    today = datetime.now()
    last_month = today.replace(day=1) - timedelta(days=1)
    month_name = last_month.strftime("%B_%Y")
    
    report_folder = Path("reports")
    report_folder.mkdir(exist_ok=True)
    
    try:
        # Load data (assuming you have CSV files)
        sales_data = pd.read_csv("data/sales.csv")
        sales_data['date'] = pd.to_datetime(sales_data['date'])
        
        # Filter for last month
        month_data = sales_data[
            (sales_data['date'].dt.month == last_month.month) &
            (sales_data['date'].dt.year == last_month.year)
        ]
        
        # Create visualizations
        create_sales_chart(month_data, report_folder, month_name)
        create_product_chart(month_data, report_folder, month_name)
        
        # Generate text report
        create_text_report(month_data, report_folder, month_name)
        
        print(f"Monthly report generated for {month_name}")
        
    except Exception as e:
        print(f"Error generating report: {e}")

def create_sales_chart(data, folder, month_name):
    """Create daily sales chart."""
    daily_sales = data.groupby(data['date'].dt.date)['total'].sum()
    
    plt.figure(figsize=(12, 6))
    plt.plot(daily_sales.index, daily_sales.values, marker='o')
    plt.title(f"Daily Sales - {month_name}")
    plt.xlabel("Date")
    plt.ylabel("Sales ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    chart_path = folder / f"daily_sales_{month_name}.png"
    plt.savefig(chart_path)
    plt.close()

def create_product_chart(data, folder, month_name):
    """Create product performance chart."""
    product_sales = data.groupby('product')['total'].sum().sort_values(ascending=False)
    
    plt.figure(figsize=(10, 6))
    product_sales.head(10).plot(kind='bar')
    plt.title(f"Top 10 Products - {month_name}")
    plt.xlabel("Product")
    plt.ylabel("Sales ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    chart_path = folder / f"top_products_{month_name}.png"
    plt.savefig(chart_path)
    plt.close()

def create_text_report(data, folder, month_name):
    """Create comprehensive text report."""
    
    report_content = f"""
MONTHLY SALES REPORT - {month_name.replace('_', ' ').title()}
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

SUMMARY STATISTICS:
- Total Sales: ${data['total'].sum():,.2f}
- Average Daily Sales: ${data.groupby(data['date'].dt.date)['total'].sum().mean():,.2f}
- Total Orders: {len(data):,}
- Average Order Value: ${data['total'].mean():.2f}

TOP PERFORMING PRODUCTS:
"""
    
    top_products = data.groupby('product')['total'].sum().sort_values(ascending=False).head(5)
    for i, (product, sales) in enumerate(top_products.items(), 1):
        report_content += f"{i}. {product}: ${sales:,.2f}\n"
    
    report_content += f"""

DAILY BREAKDOWN:
"""
    
    daily_sales = data.groupby(data['date'].dt.date)['total'].sum()
    for date, sales in daily_sales.items():
        report_content += f"{date}: ${sales:,.2f}\n"
    
    # Save report
    report_path = folder / f"monthly_report_{month_name}.txt"
    with open(report_path, 'w') as f:
        f.write(report_content)

# Schedule to run on the 1st of every month
schedule.every().month.do(generate_monthly_report)
```

## Scheduling Your Automation

### Using the `schedule` Library

```python
import schedule
import time

# Install with: pip install schedule

def my_automation_task():
    print("Running automation...")
    # Your automation code here

# Different scheduling options:

# Every day at specific time
schedule.every().day.at("09:00").do(my_automation_task)

# Every hour
schedule.every().hour.do(my_automation_task)

# Every Monday
schedule.every().monday.do(my_automation_task)

# Every 30 minutes
schedule.every(30).minutes.do(my_automation_task)

# Multiple schedules
schedule.every().day.at("09:00").do(organize_downloads)
schedule.every().hour.do(backup_important_files)
schedule.every().monday.at("08:00").do(generate_weekly_report)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
```

### Using Windows Task Scheduler

Create a batch file (`run_automation.bat`):
```batch
@echo off
cd /d "C:\path\to\your\script"
python file_organizer.py
pause
```

### Using macOS/Linux Cron

Edit crontab with `crontab -e`:
```bash
# Run every day at 9 AM
0 9 * * * /usr/bin/python3 /path/to/your/script/file_organizer.py

# Run every hour
0 * * * * /usr/bin/python3 /path/to/your/script/file_organizer.py

# Run every Monday at 8 AM
0 8 * * 1 /usr/bin/python3 /path/to/your/script/file_organizer.py
```

## Error Handling and Logging

```python
import logging
import traceback
from datetime import datetime

def setup_robust_logging():
    """Set up comprehensive logging for automation scripts."""
    
    # Create logs directory
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    # Configure logging
    log_filename = log_dir / f"automation_{datetime.now().strftime('%Y%m%d')}.log"
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler()  # Also print to console
        ]
    )
    
    return logging.getLogger(__name__)

def safe_automation_wrapper(func):
    """Decorator to safely run automation functions with error handling."""
    
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(__name__)
        
        try:
            logger.info(f"Starting {func.__name__}")
            result = func(*args, **kwargs)
            logger.info(f"Successfully completed {func.__name__}")
            return result
            
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {str(e)}")
            logger.error(f"Full traceback: {traceback.format_exc()}")
            
            # Optional: Send error notification
            send_error_notification(func.__name__, str(e))
            
        except KeyboardInterrupt:
            logger.info(f"User interrupted {func.__name__}")
            
    return wrapper

def send_error_notification(function_name, error_message):
    """Send notification when automation fails."""
    
    # Email notification
    try:
        # Implement email sending logic here
        print(f"ERROR ALERT: {function_name} failed with: {error_message}")
    except:
        pass  # Don't let notification errors break the main script

# Use the decorator on your automation functions
@safe_automation_wrapper
def organize_files():
    # Your file organization code here
    pass

@safe_automation_wrapper  
def backup_data():
    # Your backup code here
    pass
```

## Best Practices for Automation

### 1. Start Small and Simple
```python
# Good: Start with basic functionality
def organize_downloads_basic():
    """Simple file organizer - start here!"""
    downloads = Path.home() / "Downloads"
    
    for file in downloads.iterdir():
        if file.suffix == ".pdf":
            pdf_folder = downloads / "PDFs"
            pdf_folder.mkdir(exist_ok=True)
            file.rename(pdf_folder / file.name)

# Then expand gradually with more features
```

### 2. Test in Dry-Run Mode
```python
def organize_files(dry_run=True):
    """Always include a dry-run option for testing."""
    
    for file_path in source_folder.iterdir():
        destination = get_destination(file_path)
        
        if dry_run:
            print(f"Would move: {file_path} → {destination}")
        else:
            shutil.move(str(file_path), str(destination))
            print(f"Moved: {file_path} → {destination}")
```

### 3. Make It Configurable
```python
# Use configuration files for flexibility
config = {
    "source_folder": "/Users/username/Downloads",
    "categories": {
        "Documents": [".pdf", ".doc", ".docx"],
        "Images": [".jpg", ".png", ".gif"]
    },
    "schedule": "daily",
    "time": "09:00"
}
```

### 4. Add Progress Indicators
```python
from tqdm import tqdm  # pip install tqdm

def organize_files_with_progress():
    """Show progress for long-running operations."""
    
    files = list(source_folder.iterdir())
    
    for file_path in tqdm(files, desc="Organizing files"):
        # Process each file
        time.sleep(0.1)  # Simulate work
        process_file(file_path)
```

### 5. Handle Edge Cases
```python
def robust_file_organizer():
    """Handle common edge cases."""
    
    try:
        for file_path in source_folder.iterdir():
            # Skip system files
            if file_path.name.startswith('.'):
                continue
                
            # Skip files currently in use
            if is_file_in_use(file_path):
                logger.warning(f"Skipping file in use: {file_path}")
                continue
                
            # Handle permission errors
            try:
                process_file(file_path)
            except PermissionError:
                logger.error(f"Permission denied: {file_path}")
                continue
                
    except Exception as e:
        logger.error(f"Unexpected error: {e}")

def is_file_in_use(file_path):
    """Check if file is currently being used."""
    try:
        with open(file_path, 'r+'):
            return False
    except IOError:
        return True
```

## Testing Your Automation

```python
import unittest
import tempfile
import shutil
from pathlib import Path

class TestFileOrganizer(unittest.TestCase):
    """Test your automation functions."""
    
    def setUp(self):
        """Create temporary test environment."""
        self.test_dir = Path(tempfile.mkdtemp())
        
        # Create test files
        (self.test_dir / "document.pdf").touch()
        (self.test_dir / "image.jpg").touch()
        (self.test_dir / "video.mp4").touch()
    
    def tearDown(self):
        """Clean up test environment."""
        shutil.rmtree(self.test_dir)
    
    def test_file_organization(self):
        """Test that files are organized correctly."""
        organize_folder(self.test_dir)
        
        # Check that folders were created
        self.assertTrue((self.test_dir / "Documents").exists())
        self.assertTrue((self.test_dir / "Images").exists())
        self.assertTrue((self.test_dir / "Videos").exists())
        
        # Check that files were moved
        self.assertTrue((self.test_dir / "Documents" / "document.pdf").exists())
        self.assertTrue((self.test_dir / "Images" / "image.jpg").exists())
        self.assertTrue((self.test_dir / "Videos" / "video.mp4").exists())
    
    def test_duplicate_handling(self):
        """Test handling of duplicate filenames."""
        # Create duplicate files
        (self.test_dir / "Documents").mkdir()
        (self.test_dir / "Documents" / "document.pdf").touch()
        
        organize_folder(self.test_dir)
        
        # Check that duplicate was renamed
        self.assertTrue((self.test_dir / "Documents" / "document_1.pdf").exists())

if __name__ == "__main__":
    unittest.main()
```

## Expanding Your Automation Skills

### Next Steps for Learning

1. **Learn More Libraries**:
   - `selenium` - Web browser automation
   - `beautifulsoup4` - Web scraping
   - `openpyxl` - Advanced Excel manipulation
   - `pillow` - Image processing
   - `psutil` - System monitoring

2. **Advanced Automation Ideas**:
   - Social media posting automation
   - Invoice processing and data extraction
   - Automated testing of web applications
   - System monitoring and alerting
   - Data pipeline automation

3. **Integration with Cloud Services**:
   - Google Drive/Dropbox automation
   - Email marketing automation
   - Database automation
   - API integrations

### Example: Advanced Web Automation

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def automate_data_entry():
    """Automate repetitive web form filling."""
    
    # Set up web driver (requires ChromeDriver)
    driver = webdriver.Chrome()
    
    try:
        # Open the website
        driver.get("https://example-form.com")
        
        # Fill out form fields
        name_field = driver.find_element(By.NAME, "name")
        name_field.send_keys("John Doe")
        
        email_field = driver.find_element(By.NAME, "email")
        email_field.send_keys("john@example.com")
        
        # Submit form
        submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
        submit_button.click()
        
        time.sleep(2)  # Wait for confirmation
        
        print("Form submitted successfully!")
        
    finally:
        driver.quit()

# Schedule this to run automatically
schedule.every().day.at("10:00").do(automate_data_entry)
```

---

## Summary

Automation with Python can transform how you work by:

- **Eliminating repetitive tasks** like file organization
- **Reducing human error** through consistent processes
- **Saving hours of time** every week
- **Running tasks while you sleep** with scheduling
- **Scaling your productivity** beyond manual limits

**Start your automation journey:**

1. **Pick one repetitive task** you do regularly
2. **Write a simple Python script** to automate it
3. **Test thoroughly** with dry-run mode
4. **Add error handling** and logging
5. **Schedule it to run automatically**
6. **Expand with more features** over time

Remember: The best automation is the one you actually use. Start simple, test thoroughly, and gradually add more features as you become comfortable with the basics.

*The file organizer example in this guide can save you hours every month. Imagine what other automations you could create!*