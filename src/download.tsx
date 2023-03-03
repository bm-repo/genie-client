export const downloadFile = async (props: DownloadProps) => {
    const blob = new Blob([props.content.toString()], { type: props.type });
    const url = window.URL.createObjectURL(blob);
    const link1 = document.createElement(aTag);
    const link = link1;
    link.href = url;
    link.setAttribute(downloadAttr, props.fileName);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link); 
}
