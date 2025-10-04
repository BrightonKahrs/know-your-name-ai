variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
  default     = "rg-knowyourname-dev"
}

variable "location" {
  description = "Azure region for resources"
  type        = string
  default     = "East US"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "development"
}

variable "project_name" {
  description = "Name of the project"
  type        = string
  default     = "knowyourname"
}

variable "storage_account_name" {
  description = "Name of the storage account for Terraform state"
  type        = string
  default     = "tfstateknowname001"
}

variable "aks_cluster_name" {
  description = "Name of the AKS cluster"
  type        = string
  default     = "aks-knowyourname-dev"
}

variable "postgresql_server_name" {
  description = "Name of the PostgreSQL server"
  type        = string
  default     = "psql-knowyourname-dev"
}

variable "api_management_name" {
  description = "Name of the API Management service"
  type        = string
  default     = "apim-knowyourname-dev"
}

variable "tags" {
  description = "Tags to apply to resources"
  type        = map(string)
  default = {
    Environment = "development"
    Project     = "know-your-name-ai"
    ManagedBy   = "terraform"
  }
}

variable "node_count" {
  description = "Number of nodes in the AKS cluster"
  type        = number
  default     = 2
}

variable "vm_size" {
  description = "Size of the AKS nodes"
  type        = string
  default     = "Standard_D2s_v3"
}
