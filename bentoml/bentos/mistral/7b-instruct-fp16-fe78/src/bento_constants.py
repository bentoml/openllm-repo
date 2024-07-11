
CONSTANT_YAML = '''
chat_template: mistral-instruct
engine_config:
  dtype: half
  enforce_eager: true
  max_model_len: 1024
  model: mistralai/Mistral-7B-Instruct-v0.1
extra_labels:
  openllm_alias: 7b,7b-instruct
  openllm_hf_model_id: mistralai/Mistral-7B-Instruct-v0.1
project: vllm-chat
service_config:
  name: mistral
  resources:
    gpu: 1
    gpu_type: nvidia-tesla-l4
  traffic:
    timeout: 300

'''