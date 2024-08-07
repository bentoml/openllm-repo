
CONSTANT_YAML = '''
engine_config:
  max_model_len: 2048
  model: meta-llama/Meta-Llama-3-70B-Instruct
  tensor_parallel_size: 2
extra_labels:
  model_name: meta-llama/Meta-Llama-3-70B-Instruct
  openllm_alias: 70b,70b-instruct
project: vllm-chat
service_config:
  name: llama3
  resources:
    gpu: 2
    gpu_type: nvidia-a100-80g
  traffic:
    timeout: 300

'''
