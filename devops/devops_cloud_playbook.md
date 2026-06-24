# DevOps & Cloud Engineering Playbook

## Overview
This playbook provides strict templates for generating Infrastructure as Code (IaC), CI/CD pipelines, and containerization strategies for seamless deployment.

## 1. Dockerization

### Prompt Template
```markdown
Context:
- App Stack: {e.g., Node.js, Spring Boot, Go}
- Port constraints: {e.g., 8080}

Task:
1. Write a multi-stage `Dockerfile` optimized for production.
2. Ensure the final image uses a distroless or alpine base image for security.
3. Run the application as a non-root user.
4. Provide the `.dockerignore` file.
5. **VERIFICATION REQUIRED**: You MUST successfully execute `docker build -t test-build .` to verify syntax before considering this task complete.
```

## 2. CI/CD Pipeline Setup

### Prompt Template
```markdown
Context:
- Target platform: {GitHub Actions / GitLab CI}
- Deployment target: {AWS ECS, Vercel, Google Play Store}

Task:
1. Create a CI pipeline that runs linting, unit tests, and security scans on every PR.
2. Create a CD pipeline that builds the Docker image, tags it with the Git SHA, and deploys it on merge to `main`.
3. Extract all sensitive secrets to environment variables (e.g., `${{ secrets.AWS_ACCESS_KEY_ID }}`).
```

## 3. Infrastructure as Code (Terraform)

### Prompt Template
```markdown
Context:
- Cloud Provider: {AWS / GCP / Azure}
- Required Resources: {e.g., VPC, RDS PostgreSQL, ECS Cluster, Load Balancer}

Task:
1. Write the Terraform (`.tf`) files to provision the requested architecture.
2. Adhere to the principle of least privilege for IAM roles.
3. Output all relevant connection strings/ARNs as Terraform outputs.
4. Modularize the setup (e.g., network, database, compute).
```
