from_pretrained(model_name,num_labels=2)
output = output["logits"].detach()[:,1].reshape((-1))

from_pretrained(model_name,num_labels=1)
output = output["logits”].squeeze(-1)
