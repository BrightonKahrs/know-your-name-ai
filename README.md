# Know Your Name AI

An AI-powered application that helps users discover interesting information about their names, including origin, meaning, cultural significance, and famous people who share their name.

## 🎯 Learning Goals

This repository is designed to explore and learn about:

- **Azure Kubernetes Service (AKS)** - Container orchestration based on OSS Kubernetes
- **Azure PostgreSQL Flexible Server** - Managed database service based on OSS PostgreSQL
- **API Management + AI** - Azure API Management with AI-powered services
- **Python & FastAPI** - Modern async web API development
- **Flask** - Lightweight web application framework
- **Terraform (OSS)** - Infrastructure as Code
- **Load Testing with Locust (OSS)** - Performance testing
- **E2E Testing with Playwright (OSS)** - Browser automation and testing
- **GitHub Copilot** - AI-assisted development
- **Cloud-native architecture** and networking best practices

## Architecture

This application follows a microservices architecture deployed on Azure Kubernetes Service:

- **API Service**: Python FastAPI with AI-powered name analysis
- **Web Service**: Flask-based frontend application
- **PostgreSQL**: Managed database for storing name analysis data
- **API Management**: Gateway and API management layer
- **Container Registry**: Azure Container Registry for Docker images

## Repository Structure

```
know-your-name-ai/
├── src/                          # Main application code
│   ├── backend/                  # FastAPI backend service
│   │   ├── main.py
│   │   ├── requirements.txt
│   │   ├── Dockerfile
│   │   └── backend-venv/         # Python virtual environment
│   └── frontend/                 # Flask frontend service
│       ├── app.py
│       ├── requirements.txt
│       ├── Dockerfile
│       ├── templates/
│       ├── static/
│       └── frontend-venv/        # Python virtual environment
├── infrastructure/               # Terraform infrastructure code
│   ├── main.tf
│   ├── aks.tf
│   ├── postgresql.tf
│   └── api-management.tf
├── k8s/                         # Kubernetes manifests
│   ├── backend-deployment.yaml
│   ├── frontend-deployment.yaml
│   └── ingress.yaml
├── tests/                       # Testing framework
│   ├── load-tests/              # Locust load tests
│   ├── e2e-tests/               # Playwright E2E tests
│   └── unit-tests/              # Python unit tests
├── .github/workflows/           # CI/CD pipelines
│   ├── build-and-test.yml
│   ├── deploy-to-aks.yml
│   └── terraform-plan.yml
└── docker-compose.yml           # Local development setup
```

## Getting Started

### Prerequisites

- [Python 3.11+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started)
- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
- [Terraform](https://www.terraform.io/downloads.html)
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

### Local Development

1. **Clone the repository**

   ```bash
   git clone https://github.com/BrightonKahrs/know-your-name-ai.git
   cd know-your-name-ai
   ```

2. **Build and run with Docker Compose**

   ```bash
   docker-compose up --build
   ```

3. **Or run individually**

   ```bash
   # Backend API
   cd src/backend
   python -m venv backend-venv
   backend-venv\Scripts\activate  # On Windows
   # source backend-venv/bin/activate  # On Linux/macOS
   pip install -r requirements.txt
   python main.py

   # Frontend
   cd src/frontend
   python -m venv frontend-venv
   frontend-venv\Scripts\activate  # On Windows
   # source frontend-venv/bin/activate  # On Linux/macOS
   pip install -r requirements.txt
   python app.py
   ```

### Testing

- **Unit Tests**: `cd tests/unit-tests && python -m pytest`
- **Load Tests**: `cd tests/load-tests && locust --host http://localhost:8000`
- **E2E Tests**: `cd tests/e2e-tests && npx playwright test`

## ☁️ Azure Deployment

### Infrastructure Setup

1. **Deploy infrastructure with Terraform**

   ```bash
   cd infrastructure
   terraform init
   terraform plan
   terraform apply
   ```

2. **Deploy applications to AKS**

   ```bash
   # Get AKS credentials
   az aks get-credentials --resource-group rg-knowyourname-dev --name aks-knowyourname-dev

   # Deploy applications
   kubectl apply -f k8s/
   ```

### CI/CD Pipeline

The repository includes GitHub Actions workflows for:

- **Build and Test**: Automated testing on every PR
- **Infrastructure**: Terraform plan/apply for infrastructure changes
- **Deployment**: Automated deployment to AKS on main branch

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with love for learning cloud-native technologies
- Powered by open source software
- Enhanced with GitHub Copilot
