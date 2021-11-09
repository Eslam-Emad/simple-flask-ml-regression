import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


class Repository:
    @staticmethod
    def make_picture(training_data_filename, model, new_input, save_file=False):
        data = pd.read_pickle(training_data_filename)
        ages = data['Age']
        data = data[ages > 0]
        ages = data['Age']
        heights = data['Height']
        x_new = np.arange(18).reshape((18, 1))
        preds = model.predict(x_new)

        fig = px.scatter(x=ages, y=heights, title="Height vs Age", labels={'x': 'Age (Years)', 'y': 'Height (Inches)'})
        fig.add_trace(go.Scatter(x=x_new.reshape(x_new.shape[0]), y=preds, mode='lines', name='Model'))

        if new_input is not False:
            new_pred = model.predict(new_input)
            fig.add_trace(go.Scatter(x=new_input.reshape(len(new_input)), y=new_pred, mode='lines', name='New Outputs',
                                     marker=dict(color='green', size=20, line=dict(color='green', width=2))))

        if save_file:
            fig.write_image(save_file, width=800, engine='kaleido')

        return fig

    @staticmethod
    def floats_string_to_input_arr(floats_str):
        floats = [float(x.strip()) for x in floats_str.split(',')]
        as_np_arr = np.array(floats).reshape(len(floats), 1)
        return as_np_arr
