FROM darribas/gds_py:7.0

# Local docs
RUN rm -R work/
RUN mkdir ${HOME}/content
COPY ./content ${HOME}/content

# Update to recent libs
#RUN pip install -U --no-deps contextily seaborn

# Fix permissions
USER root
RUN chown -R ${NB_UID} ${HOME}
RUN rm -rf ${HOME}/content/pages
USER ${NB_USER}
