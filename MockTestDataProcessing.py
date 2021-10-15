from kubernetes import client, config
from robot.api import logger

class MockTestDataProcessing:
    def trigger_segment_processing(self,job_name,cron_job_name,namespace):
        config.load_kube_config()
        batch_v1 = client.BatchV1Api()
        batch_v1beta1 = client.BatchV1beta1Api()
        cron_job = batch_v1beta1.read_namespaced_cron_job(cron_job_name, namespace)
        job = client.V1Job(
            api_version='batch/v1',
            kind='Job',
            metadata=client.models.V1ObjectMeta(
                name=job_name,
                # This annotation is added by kubectl, probably best to add it ourselves as well
                annotations={"cronjob.kubernetes.io/instantiate": "manual"}
            ),
            spec=cron_job.spec.job_template.spec
        )

        result = batch_v1.create_namespaced_job(namespace, job)
        logger.info(result)

        pass

    def trigger_data_transfer_job(self,transfer_job_name):
        pass
