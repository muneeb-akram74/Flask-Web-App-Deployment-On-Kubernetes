# Flask Web App Deployment on Kubernetes 

This project demonstrates how to **containerize and deploy a Flask web application** on a **Kubernetes cluster using Minikube**. It serves as a hands-on guide for beginners to learn Kubernetes fundamentals. 

##  Project Overview

- Develop a **Flask web app** and package it as a **Docker container**  
- Deploy the application on **Kubernetes** using **Deployments and Services**  
- Use **Minikube** to create a local Kubernetes cluster  
- Expose the application externally using a **NodePort Service**  
- Debug common Kubernetes issues like **CrashLoopBackOff** and networking errors  
- Scale the application dynamically using `kubectl scale`  

---

##  Getting Started

### **1 Prerequisites**
Ensure you have the following installed:
- [Docker](https://docs.docker.com/get-docker/)
- [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)

### **2 Clone the Repository**
```sh
git clone https://github.com/MuneebAkram/flask-k8s-app.git
cd flask-k8s-app
```

### **3 Build the Docker Image**
```sh
docker build -t muneebakram/flask-k8s-app .
```

### **4 Start Minikube**
If virtualization is disabled in BIOS, use Docker as the driver:
```sh
minikube start --driver=docker
```

### **5 Deploy to Kubernetes**
```sh
kubectl apply -f flask-deployment.yaml
kubectl apply -f flask-service.yaml
```

### **6 Get the Minikube IP and NodePort**
```sh
minikube ip
kubectl get services
```
Find the NodePort and access the app at:
```
http://<minikube-ip>:<NodePort>
```
Or run:
```sh
minikube service flask-service --url
```

---

## Troubleshooting

### **Minikube Start Fails Due to Virtualization**
 **Solution:** Run Minikube with Docker driver:  
```sh
minikube start --driver=docker
```

###  **Pod Stuck in CrashLoopBackOff**
 **Solution:** Check pod logs to find errors:
```sh
kubectl logs <pod-name>
```
Fix the issue, rebuild the image, and update the deployment.

###  **Cannot Access the Web App**
 **Solution:** Ensure Minikube is running and use the correct IP & NodePort:
```sh
minikube ip
kubectl get services
```

---

##  Key Learnings

 **Containerization with Docker**  
 **Deploying applications on Kubernetes**  
 **Exposing services using NodePort**  
 **Debugging Kubernetes deployments**  
 **Scaling applications in Kubernetes**  

---

## 📜 License
This project is licensed under the [MIT License](LICENSE).

##  Contributing
Feel free to **fork** this repository and submit **pull requests**. Let's learn and grow together! 💡

---

##  Author
**Muneeb Akram**  
- Follow my journey on **[LinkedIn](https://www.linkedin.com/in/muneeb74/)**  
- View my other projects on **[GitHub](https://github.com/muneeb-akram74)**

