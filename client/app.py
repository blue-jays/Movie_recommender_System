import gradio as gr

def add_marks(math, physics, chemistry):
    total = math + physics + chemistry
    if total <0:
        result = "Wrong input"
    elif total < 50:
        result = "Fail"
    else:
        result = "Pass"
    return total, result



with gr.Blocks() as demo:
    gr.Markdown("Result Calculator")
    
    
    
    with gr.Row():
        with gr.Column():
            math = gr.Number(label ="Math")
            physics = gr.Number(label = "Physics")
            chemistry = gr.Number(label = "Chemistry")   
            
            button = gr.Button("Add")
            
                 
        with gr.Column():
            Total = gr.Number(label="Total")
            Result = gr.Textbox(label = "Result")
            
   
            
    button.click(fn = add_marks, inputs= [math, physics, chemistry], outputs=[Total, Result])
    

demo.launch()