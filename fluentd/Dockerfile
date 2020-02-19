FROM fluentd
USER root
COPY fluent.conf /fluentd/etc/fluent.conf
RUN echo "poc 192.168.1.246" >> /etc/hosts
RUN /usr/bin/fluent-gem install fluent-plugin-elasticsearch fluent-plugin-s3
USER fluent

