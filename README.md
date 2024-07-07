# QR Code Generator CLI

This project provides a QR code generator with additional features like adding logos and text below the QR code. A Command Line Interface (CLI) is provided for ease of use.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Samples](#samples)
- [Contributing](#contributing)
- [License](#license)


## Features

- Generate QR codes for URLs.
- Customize QR codes with logos.
- Add text below the QR codes.
- Configurable via a JSON file.
- Docker support for containerized deployment.
- Automated CI/CD pipeline with GitHub Actions.

## Project Structure



## Setup

### Prerequisites

- Python 3.10 or higher
- Docker (optional, for containerized usage)
- Make (optional, for using the Makefile)

### Installation

1. Clone the repository:

   ```bash 
   git clone https://github.com/ajakaiye33/qr_code_generator.git```

   ```bash cd qr_code_generator```


2. Install the required Python packages:

```make install```


### Configuration

Create a configuration file at config/config.json with the following content:

```
{
  "logo_path": "./image/icononly_transparent_nobuffer.png",
  "font_path": "./image/DejaVuSans-Bold.ttf",
  "output_dir": "./output"
}
```

### Usage

Generate QR codes via the CLI:
 ```bash python main.py``` or 
 ```bash python app.py --config config/config.json --output ./output```

### Samples

Here are some samples of the generated QR codes:

![Linkedin QR Code profile](sample_qrcode_images/linkedin_profile_qrcode_with_text_2.png)   ![Github QR Code Profile](sample_qrcode_images/github.png)

![X QR Code Profile](sample_qrcode_images/twitterprofile.png)  ![Youtube QR Code Profile](sample_qrcode_images/social_media_profile_qrcode_with_text_1.png)

![Snapchat QR Code Profile](sample_qrcode_images/social_media_profile_qrcode_with_text_2.png) ![Github QR Code Profile](sample_qrcode_images/guido.png)

... now go generate yours :wink:

### Contributing

Contributions are welcome! Please fork the repository and create a pull request.

- Fork the repository
- Create a new branch (git checkout -b feature-branch)
- Commit your changes (git commit -am 'Add new feature')
- Push to the branch (git push origin feature-branch)
- Create a new Pull Request

### License

This project is licensed under the MIT License. See the LICENSE file for details.
