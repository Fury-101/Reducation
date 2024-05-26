export async function load({ params }) {
    const apiPort = 5000

    let d = await fetch(`http://localhost:${apiPort}/get_curriculum`, {
        method: 'POST',
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
        },
        body: JSON.stringify({'input_string': params.slug})
    });
    d = await d.json()
    return {
        slug: params.slug,
        data: {
            d
        }
    }
}
export const ssr = false