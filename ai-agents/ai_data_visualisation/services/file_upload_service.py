def upload_dataset(code_interpreter, uploaded_file, st) -> str:
    """Upload a dataset to the E2B sandbox."""
    dataset_path = f"./{uploaded_file.name}"

    try:
        code_interpreter.files.write(dataset_path, uploaded_file)
        return dataset_path
    except Exception as error:
        st.error(f"Error during file upload: {error}")
        raise error