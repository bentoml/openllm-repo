
CONSTANT_YAML = '''
engine_config:
  dtype: half
  max_model_len: 2048
  model: google/gemma-7b-it
extra_labels:
  openllm_alias: 7b,7b-instruct
  openllm_hf_model_id: google/gemma-7b-it
project: vllm-chat
service_config:
  name: gemma
  resources:
    gpu: 1
    gpu_type: nvidia-tesla-l4
  traffic:
    timeout: 300

'''