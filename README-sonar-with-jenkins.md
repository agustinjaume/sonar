## Objetivo realizar pruebas de integracion con Jenkins y Sonarqube

En este video veremos los concepto de Sonar y como conectarlo con Jenkins para poder realizar pruebas de integracion, con cada merge de github.

## Components to see

-  Jenkins server and JDK installed in nodes
-  Sonarqube 
-  Sonar Plugin for Jenkins
-  Code of basic aplication

### Jenkins Server 

- https://github.com/agustinjaume/jenkins-server   ( the best tutorial )

### Sonarqube

- https://www.sonarqube.org/
- https://github.com/SonarSource/docker-sonarqube

- Versions: 
    - Community
    - Develop
    - Enterprise
    - Data Center

### Create and deploy personality version

```

cd docker
docker build -t "sonar-ideasextraordinarias:v1" .   ( en localhost)
<!-- 
docker  tag  sonar-ideasextraordinarias:v1  aguexitoso/sonar-ideasextraordinarias:v1  ( para subir a registro publico ) 
docker login 
docker push aguexitoso/sonar-ideasextraordinarias:v1 
-->

docker run -d --name sonarqube -p 9000:9000 sonar-ideasextraordinarias:v1

```

###  Sonar Plugin for Jenkins

- https://docs.sonarqube.org/latest/analysis/scan/sonarscanner-for-jenkins/

- Open Jenkins server and we go  to configuration in Jenkins --> Manage Jenkins --> Manage Plugins --> find " SonarQube Scanner for Jenkins" and install.
- After reboot Jenkins we go to Jenkins --> Manage Jenkins --> Global Tool Configuration --> we go to Sonar block.
- 


###  Code of basic aplication

### Deploy


Log in to http://localhost:9000 with System Administrator credentials (login=admin, password=admin).


### Sonarscanner


Sonar Scanner : The SonarScanner is the scanner to use when there is no specific scanner for your build system.
Once the SonarQube platform has been installed, you're ready to install a scanner and begin creating projects. To do that, you must install and configure the scanner that is most appropriate for your needs. Do you build with

Scanners
SonarScanner for Gradle
SonarScanner for MSBuild
SonarScanner for Maven
SonarScanner for Azure DevOps
SonarScanner for Jenkins
SonarScanner for Ant
SonarScanner


### Deploy test with Sonarqube only 


Steps

- New Project and define name
- Create token, and we will define name token, after copy token in secure zone   example : frontend-app1-token: e860a7ae57d17125df16570b489a200308a0eaf8
- Define technology:
    - "Java"
    - "C# or VB.NET"
    - "Other (JS, TS, Go, Python, PHP, ...)"
- Define OS 
    - Linux
    - Windows
    - macOS
- Download and unzip the Scanner for Linux
- Create a configuration file in your project's root directory called sonar-project.properties
  
```
# must be unique in a given SonarQube instance
sonar.projectKey=my:project

# --- optional properties ---

# defaults to project key
#sonar.projectName=My project
# defaults to 'not provided'
#sonar.projectVersion=1.0
 
# Path is relative to the sonar-project.properties file. Defaults to .
#sonar.sources=.
 
# Encoding of the source code. Default is default system encoding
#sonar.sourceEncoding=UTF-8
```

- Run next commands in project's folder, in ours case is /projects/frontend-app1
   
```
   sonar-scanner \
  -Dsonar.projectKey=frontend-app1 \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=e860a7ae57d17125df16570b489a200308a0eaf8
```





### Documentation 

- https://www.it-swarm.dev/es/sonarqube/
- https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/
- https://docs.sonarqube.org/latest/analysis/scan/sonarscanner-for-jenkins/
- https://www.it-swarm.dev/es/sonarqube/existen-otras-herramientas-de-gestion-de-calidad-que-no-sean-sonarqube/971093933/