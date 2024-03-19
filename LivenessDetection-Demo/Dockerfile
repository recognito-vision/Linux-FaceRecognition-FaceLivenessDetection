FROM ubuntu:20.04

# Set the timezone of the container
ENV CONTAINER_TIMEZONE=UTC
RUN ln -snf /usr/share/zoneinfo/$CONTAINER_TIMEZONE /etc/localtime && echo $CONTAINER_TIMEZONE > /etc/timezone

# Create directory for the application
RUN mkdir -p /home/recognito_fl

# Set the working directory
WORKDIR /home/recognito_fl

# Copy the application files into the container
COPY . .

# Make the scripts executable
RUN chmod +x install.sh run_demo.sh

# Run the install.sh script to perform any installation tasks
RUN apt-get update && apt-get install -y sudo
RUN ./install.sh

# Expose port 8000(flask), 7860(gradio)
EXPOSE 8000 7860

# Set the default command to run the application
ENTRYPOINT ["./run_demo.sh"]
